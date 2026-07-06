# 1. Import libraries

from flask import Flask, render_template, request, redirect
import json
import os
import duckdb
from datetime import date


# 2. Set up Flask app and file paths

app = Flask(__name__)

DATA_FILE = "data/cafe_sales.json"


# 3. Define helper functions

def load_orders():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_orders(orders):
    with open(DATA_FILE, "w") as file:
        json.dump(orders, file, indent=4)


def generate_sales_report():
    con = duckdb.connect()

    drink_sales = con.execute(f"""
        SELECT
            drink_name,
            category,
            SUM(quantity) AS total_quantity_sold,
            ROUND(SUM(quantity * unit_price), 2) AS total_revenue,
            ROUND(AVG(customer_rating), 2) AS average_rating
        FROM read_json_auto('{DATA_FILE}')
        GROUP BY drink_name, category
        ORDER BY total_revenue DESC
    """).df()

    payment_status = con.execute(f"""
        SELECT
            payment_status,
            COUNT(*) AS number_of_orders,
            SUM(quantity) AS total_quantity,
            ROUND(SUM(quantity * unit_price), 2) AS total_amount
        FROM read_json_auto('{DATA_FILE}')
        GROUP BY payment_status
        ORDER BY payment_status
    """).df()

    category_summary = con.execute(f"""
        SELECT
            category,
            SUM(quantity) AS total_quantity_sold,
            ROUND(SUM(quantity * unit_price), 2) AS total_revenue,
            ROUND(AVG(customer_rating), 2) AS average_rating
        FROM read_json_auto('{DATA_FILE}')
        GROUP BY category
        ORDER BY total_revenue DESC
    """).df()

    con.close()

    return {
        "drink_sales": drink_sales.to_dict("records"),
        "payment_status": payment_status.to_dict("records"),
        "category_summary": category_summary.to_dict("records")
    }


def generate_boss_notes():
    con = duckdb.connect()

    highest_revenue_drink = con.execute(f"""
        SELECT
            drink_name,
            ROUND(SUM(quantity * unit_price), 2) AS total_revenue
        FROM read_json_auto('{DATA_FILE}')
        GROUP BY drink_name
        ORDER BY total_revenue DESC
        LIMIT 1
    """).fetchone()

    highest_rating_drink = con.execute(f"""
        SELECT
            drink_name,
            ROUND(AVG(customer_rating), 2) AS average_rating
        FROM read_json_auto('{DATA_FILE}')
        GROUP BY drink_name
        ORDER BY average_rating DESC
        LIMIT 1
    """).fetchone()

    lowest_rating_drink = con.execute(f"""
        SELECT
            drink_name,
            ROUND(AVG(customer_rating), 2) AS average_rating
        FROM read_json_auto('{DATA_FILE}')
        GROUP BY drink_name
        ORDER BY average_rating ASC
        LIMIT 1
    """).fetchone()

    highest_Unpaid_customer = con.execute(f"""
        SELECT
            customer_name,
            ROUND(SUM(quantity * unit_price), 2) AS Unpaid_amount
        FROM read_json_auto('{DATA_FILE}')
        WHERE payment_status = 'Unpaid'
        GROUP BY customer_name
        ORDER BY Unpaid_amount DESC
        LIMIT 1
    """).fetchone()

    strongest_category = con.execute(f"""
        SELECT
            category,
            ROUND(SUM(quantity * unit_price), 2) AS total_revenue
        FROM read_json_auto('{DATA_FILE}')
        GROUP BY category
        ORDER BY total_revenue DESC
        LIMIT 1
    """).fetchone()

    con.close()

    boss_notes = []

    if highest_revenue_drink:
        boss_notes.append(
            f"Best revenue drink: {highest_revenue_drink[0]} generated the highest total revenue of ${highest_revenue_drink[1]}."
        )

    if highest_rating_drink:
        boss_notes.append(
            f"Best rated drink: {highest_rating_drink[0]} received the highest average customer rating of {highest_rating_drink[1]}."
        )

    if lowest_rating_drink:
        boss_notes.append(
            f"Drink to review: {lowest_rating_drink[0]} received the lowest average customer rating of {lowest_rating_drink[1]}."
        )

    if highest_Unpaid_customer:
        boss_notes.append(
            f"Customer to follow up: {highest_Unpaid_customer[0]} has the highest Unpaid amount of ${highest_Unpaid_customer[1]}."
        )
    else:
        boss_notes.append(
            "Payment follow-up: There are no Unpaid customer balances at the moment."
        )

    if strongest_category:
        boss_notes.append(
            f"Category to monitor: {strongest_category[0]} generated the highest total revenue of ${strongest_category[1]}."
        )

    return boss_notes


# 4. Define Flask routes

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        orders = load_orders()

        drink_size = request.form["drink_size"]

        price_list = {
            "Small": 4.00,
            "Medium": 5.00,
            "Large": 6.00
        }

        unit_price = price_list[drink_size]

        new_order = {
            "order_id": len(orders) + 1,
            "order_date": str(date.today()),
            "customer_name": request.form["customer_name"],
            "drink_name": request.form["drink_name"],
            "category": request.form["category"],
            "quantity": int(request.form["quantity"]),
            "drink_size": drink_size,
            "unit_price": unit_price,
            "payment_status": request.form["payment_status"],
            "customer_rating": None
        }

        orders.append(new_order)
        save_orders(orders)

        return redirect("/orders")

    return render_template("index.html")


@app.route("/orders")
def orders():
    orders = load_orders()
    return render_template("orders.html", orders=orders)


@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    orders = load_orders()

    if request.method == "POST":
        order_id = int(request.form["order_id"])
        customer_rating = int(request.form["customer_rating"])
        customer_comment = request.form["customer_comment"]

        for order in orders:
            if order["order_id"] == order_id:
                order["customer_rating"] = customer_rating
                order["customer_comment"] = customer_comment

        save_orders(orders)

        return redirect("/feedback-report")

    pending_feedback_orders = []

    for order in orders:
        if order.get("customer_rating") is None:
            pending_feedback_orders.append(order)

    return render_template(
        "feedback.html",
        orders=pending_feedback_orders
    )

@app.route("/feedback-report")
def feedback_report():
    orders = load_orders()

    completed_feedback = []
    pending_feedback = []

    for order in orders:
        if order.get("customer_rating") is None:
            pending_feedback.append(order)
        else:
            completed_feedback.append(order)

    con = duckdb.connect()

    average_rating_by_drink = con.execute(f"""
        SELECT
            drink_name,
            category,
            COUNT(customer_rating) AS number_of_feedback,
            ROUND(AVG(customer_rating), 2) AS average_rating
        FROM read_json_auto('{DATA_FILE}')
        WHERE customer_rating IS NOT NULL
        GROUP BY drink_name, category
        ORDER BY average_rating DESC
    """).df()

    con.close()

    return render_template(
        "feedback_report.html",
        average_rating_by_drink=average_rating_by_drink.to_dict("records"),
        completed_feedback=completed_feedback,
        pending_feedback=pending_feedback
    )

@app.route("/sales-report")
def report():
    sales_report = generate_sales_report()
    boss_notes = generate_boss_notes()

    return render_template(
        "report.html",
        drink_sales=sales_report["drink_sales"],
        payment_status=sales_report["payment_status"],
        category_summary=sales_report["category_summary"],
        boss_notes=boss_notes
    )

@app.route("/dashboard")
def dashboard():
    import duckdb

    conn = duckdb.connect()

    conn.execute("""
        CREATE OR REPLACE TABLE cafe_sales AS
        SELECT *
        FROM read_json_auto('data/cafe_sales.json')
    """)

    # 1. Revenue by drink
    revenue_by_drink = conn.execute("""
        SELECT 
            drink_name,
            SUM(quantity * unit_price) AS total_revenue
        FROM cafe_sales
        GROUP BY drink_name
        ORDER BY total_revenue DESC
    """).fetchall()

    drink_names = [row[0] for row in revenue_by_drink]
    drink_revenues = [row[1] for row in revenue_by_drink]

    # 2. Payment status summary
    payment_summary = conn.execute("""
        SELECT
            payment_status,
            SUM(quantity * unit_price) AS total_amount
        FROM cafe_sales
        GROUP BY payment_status
        ORDER BY payment_status
    """).fetchall()

    payment_statuses = [row[0] for row in payment_summary]
    payment_amounts = [row[1] for row in payment_summary]

    # 3. Revenue by category
    category_summary = conn.execute("""
        SELECT
            category,
            SUM(quantity * unit_price) AS total_revenue
        FROM cafe_sales
        GROUP BY category
        ORDER BY total_revenue DESC
    """).fetchall()

    category_names = [row[0] for row in category_summary]
    category_revenues = [row[1] for row in category_summary]

    # 4. Average rating by drink
    rating_summary = conn.execute("""
        SELECT
            drink_name,
            AVG(customer_rating) AS average_rating
        FROM cafe_sales
        WHERE customer_rating IS NOT NULL
        GROUP BY drink_name
        ORDER BY average_rating DESC
    """).fetchall()

    rating_drink_names = [row[0] for row in rating_summary]
    drink_ratings = [round(row[1], 2) for row in rating_summary]

    conn.close()

    return render_template(
        "dashboard.html",
        drink_names=drink_names,
        drink_revenues=drink_revenues,
        rating_drink_names=rating_drink_names,
        drink_ratings=drink_ratings,
        payment_statuses=payment_statuses,
        payment_amounts=payment_amounts,
        category_names=category_names,
        category_revenues=category_revenues
    )





# 5. Run the app

if __name__ == "__main__":
    app.run(debug=True, port=5001)
    
    