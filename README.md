# Curious Bear Café App

A simple café sales and reporting app that uses Flask, JSON files, DuckDB, and basic visualization to record café orders and analyse business performance.

The app is based on a fictional café called Curious Bear Café, where Curious Bear acts as the café boss and reviews sales, feedback, payment status, and dashboard insights.

## Disclaimer

This project is for learning and educational purposes only.

It is not a production system, accounting system, point-of-sale system, or professional business reporting tool.

The café data used in this project is fictional and created for practice purposes.

## Features

* Add café orders through a Flask web form
* Store café sales data in a JSON file
* Read JSON data directly using DuckDB
* View all recorded orders
* Collect customer feedback and customer ratings
* Show pending feedback orders only in the feedback form
* Generate feedback reports
* Generate sales reports using DuckDB SQL queries
* Summarise sales by drink
* Summarise sales by category
* Summarise payment status
* Calculate average customer ratings
* Generate simple “boss notes” for Curious Bear
* Display a dashboard with chart-ready data
* Practise business-style reporting using Python, Flask, JSON, DuckDB, HTML, and CSS

## Project Structure

```text
curious-bear-cafe/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   └── cafe_sales.json
├── templates/
│   ├── index.html
│   ├── orders.html
│   ├── feedback.html
│   ├── feedback_report.html
│   ├── report.html
│   └── dashboard.html
└── static/
    └── style.css
```

Depending on the final design, the project may also include image files or additional CSS assets inside the `static/` folder.

## Requirements

* Python 3.x
* Required Python packages listed in `requirements.txt`

Suggested packages:

```text
flask
duckdb
pandas
```

## Install Python Dependencies

In the project folder, run:

```bash
pip install -r requirements.txt
```

If you are using Python 3 on macOS, you may also use:

```bash
python3 -m pip install -r requirements.txt
```

## Run the Flask App

Start the Flask app by running:

```bash
python app.py
```

or:

```bash
python3 app.py
```

If successful, the app should run locally at:

```text
http://127.0.0.1:5001
```

## App Pages

The app includes the following main pages:

```text
/
```

Main order entry page for adding new café orders.

```text
/orders
```

Displays all recorded café orders.

```text
/feedback
```

Allows feedback to be submitted for orders that have not yet received customer feedback.

```text
/feedback-report
```

Shows completed feedback, pending feedback, and average rating by drink.

```text
/sales-report
```

Shows sales analysis, payment summary, category summary, and boss notes.

```text
/dashboard
```

Shows dashboard data for visualising revenue, payment status, category performance, and customer ratings.

## Data Storage

The café sales data is stored in a JSON file:

```text
data/cafe_sales.json
```

Each order record may include fields such as:

```text
order_id
order_date
customer_name
drink_name
category
quantity
drink_size
unit_price
payment_status
customer_rating
customer_comment
```

DuckDB reads the JSON file directly using:

```sql
read_json_auto('data/cafe_sales.json')
```

This allows the app to analyse JSON data using SQL without needing a full database server.

## Sales Report

The sales report uses DuckDB SQL queries to calculate:

* Total quantity sold by drink
* Total revenue by drink
* Average rating by drink
* Number of orders by payment status
* Total amount by payment status
* Total revenue by category
* Average rating by category

This helps Curious Bear understand which drinks and categories are performing well.

## Feedback Report

The feedback report helps track customer satisfaction.

It separates:

* Completed feedback
* Pending feedback

It also calculates the average customer rating by drink using DuckDB.

## Boss Notes

The app generates simple business notes for Curious Bear, such as:

* Best revenue drink
* Best rated drink
* Drink to review
* Customer with the highest unpaid amount
* Strongest sales category

This makes the report easier to understand from a business owner’s point of view.

## Dashboard

The dashboard prepares chart data for:

* Revenue by drink
* Payment status summary
* Revenue by category
* Average rating by drink

This part connects to the visualization learning from Chapter 7 of *DuckDB Up & Running*.

## Learning Purpose

This project was created to practise using DuckDB with JSON files and to understand how data can be turned into useful reports.

It helped me practise:

* Building a Flask web app
* Saving and loading JSON data
* Reading JSON files using DuckDB
* Writing SQL queries inside Python
* Creating business-style reports
* Analysing café sales data
* Tracking payment status
* Collecting and analysing customer feedback
* Preparing data for visualization
* Connecting programming practice with accounting and business reporting

## Notes

* This project is a learning project.
* The café is fictional.
* The JSON file acts as the data source.
* DuckDB is used to query and analyse the JSON data.
* The app runs locally using Flask.
* The app has been tested locally.
* Deployment has not been tested yet.
* The project is inspired by the learning concepts from *DuckDB Up & Running*, especially Chapter 6 and Chapter 7.
* This project should not be used as a real café point-of-sale or accounting system.

## Notes for macOS and Windows Users

The commands may look slightly different depending on whether you are using macOS or Windows.

### For macOS Users

On macOS, you may need to use `python3` and `pip3`.

Install the required packages:

```bash
python3 -m pip install -r requirements.txt
```

Run the Flask app:

```bash
python3 app.py
```

If successful, open this in your browser:

```text
http://127.0.0.1:5001
```

### For Windows Users

On Windows, you can usually use `python` and `pip`.

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Flask app:

```bash
python app.py
```

If successful, open this in your browser:

```text
http://127.0.0.1:5001
```

### Important Note

Please make sure you run the commands from inside the project folder.

For example:

```bash
cd curious-bear-cafe
```

Then install the dependencies and run the app.


## Credits

This project was inspired by my learning from the book *DuckDB Up & Running* by my teacher, Mr. Go Figure Out.

The project specifically references the learning concepts from:

* Chapter 6: Using DuckDB with JSON files
* Chapter 7: Visualization

The project was further modified and extended for my own learning, including creating a café ordering flow, JSON data storage, DuckDB-powered reports, customer feedback tracking, boss notes, and dashboard-style analysis.

## Author

Created by Michelle 

## Special Thanks

My human teacher, Mr. Go Figure Out, for his encouragement.

My AI teacher, ChatGPT, for guidance.

Curious Bear, for being the café boss and making the learning journey more fun.
