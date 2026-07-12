# Curious Bear Café App

A Flask-based café sales, reporting, and customer feedback intelligence app that uses JSON files, DuckDB, SQL, rule-based sentiment analysis, and basic visualization to record café orders and analyse business performance.

The app is based on a fictional café called Curious Bear Café, where Curious Bear acts as the café boss and reviews sales, customer feedback, payment status, recurring issues, and dashboard insights.

## Disclaimer

This project is for learning and educational purposes only.

It is not a production system, accounting system, point-of-sale system, professional business reporting tool, or production-ready artificial intelligence system.

The café data used in this project is fictional and created for practice purposes.

## Features

* Add café orders through a Flask web form
* Store café sales data in a JSON file
* Read JSON data directly using DuckDB
* View all recorded orders
* Collect customer feedback and customer ratings
* Show only orders with pending feedback in the feedback form
* Generate customer feedback reports
* Classify customer comments as Positive, Neutral, or Negative
* Use predefined keywords and Python rules for sentiment classification
* Summarise sentiment results
* Identify recurring customer issues
* Generate a Client Feedback Intelligence Report
* Compare written customer comments with numerical ratings
* Generate sales reports using DuckDB SQL queries
* Summarise sales by drink
* Summarise sales by category
* Summarise payment status
* Calculate average customer ratings
* Generate simple “boss notes” for Curious Bear
* Display a dashboard with chart-ready data
* Practise business-style reporting using Python, Flask, JSON, DuckDB, SQL, HTML, and CSS

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
    ├── style.css
    └── image files
```

Depending on the final design, the project may include additional HTML templates, image files, or CSS assets inside the `templates/` and `static/` folders.

## Requirements

* Python 3.x
* Required Python packages listed in `requirements.txt`

Packages used by the project may include:

```text
flask
duckdb
pandas
```

The exact package list should follow the latest `requirements.txt` file in the repository.

## Install Python Dependencies

In the project folder, run:

```bash
pip install -r requirements.txt
```

On macOS, you may need to use:

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

The app includes the following main pages.

### Order Entry

```text
/
```

Main order entry page for adding new café orders.

### Orders

```text
/orders
```

Displays all recorded café orders.

### Customer Feedback

```text
/feedback
```

Allows feedback to be submitted for orders that have not yet received customer feedback.

### Feedback Intelligence Report

```text
/feedback-report
```

Shows completed feedback, pending feedback, average ratings, sentiment classifications, sentiment summaries, customer comments, and identified issues.

### Sales Report

```text
/sales-report
```

Shows sales analysis, payment summaries, category summaries, and boss notes.

### Dashboard

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
sentiment
```

Additional fields may be added as the project develops.

DuckDB reads the JSON file directly using:

```sql
read_json_auto('data/cafe_sales.json')
```

This allows the app to analyse JSON data using SQL without requiring a separate database server.

## Sales Report

The sales report uses DuckDB SQL queries to calculate information such as:

* Total quantity sold by drink
* Total revenue by drink
* Average rating by drink
* Number of orders by payment status
* Total amount by payment status
* Total revenue by category
* Average rating by category

This helps Curious Bear understand which drinks and categories are performing well.

## Customer Feedback Report

The customer feedback report helps Curious Bear monitor customer satisfaction and service quality.

It may include:

* Completed feedback
* Pending feedback
* Average rating by drink
* Customer comments
* Positive, Neutral, and Negative sentiment counts
* Common customer issues
* Feedback intelligence summaries

The report goes beyond numerical ratings by examining the meaning of customer comments.

For example, a customer may give a high rating but still suggest an improvement, while another customer may give a lower rating despite writing a generally positive comment. Looking at both the rating and the written feedback provides a more complete picture.

## Rule-Based Sentiment Analysis

The latest version of the Curious Bear Café App includes a rule-based sentiment analysis feature for customer comments.

The app checks customer comments against predefined positive and negative keywords and applies Python conditions to classify each comment as:

* Positive
* Neutral
* Negative

This feature does not use a pretrained machine-learning model or a pretrained sentiment classifier.

The classification logic is written directly in Python for learning purposes. This makes the rules easier to understand, test, and improve.

The rule-based approach also demonstrates an important limitation: customer language can be complex, and fixed rules may not always understand context, sarcasm, mixed opinions, or unusual wording correctly.

A possible future improvement would be to compare this rule-based approach with a trained or pretrained natural language processing model.

## Issue Detection

The app also looks for recurring issues mentioned in customer comments.

Examples may include feedback about:

* Taste
* Sweetness
* Temperature
* Waiting time
* Service
* Drink ingredients
* Portion size
* Packaging

These issue summaries help the café owner identify patterns that may not be obvious from average ratings alone.

## Boss Notes

The app generates simple business notes for Curious Bear, such as:

* Best revenue drink
* Best-rated drink
* Drink to review
* Customer with the highest unpaid amount
* Strongest sales category

This makes the reports easier to understand from a business owner’s point of view.

## Dashboard

The dashboard prepares chart data for:

* Revenue by drink
* Payment status summary
* Revenue by category
* Average rating by drink

This part connects to the visualization learning from Chapter 7 of *DuckDB Up & Running*.

## Learning Purpose

This project was created to practise using DuckDB with JSON files and to understand how structured and unstructured data can be turned into useful business insights.

It helped me practise:

* Building a Flask web app
* Saving and loading JSON data
* Reading JSON files using DuckDB
* Writing SQL queries inside Python
* Creating business-style reports
* Analysing café sales data
* Tracking payment status
* Collecting and analysing customer feedback
* Applying rule-based sentiment analysis
* Classifying comments as Positive, Neutral, or Negative
* Identifying recurring customer issues
* Comparing numerical ratings with written comments
* Preparing data for visualization
* Connecting programming practice with practical business reporting

## Project Development Journey

The project began as a simple café ordering and sales reporting app.

It was later expanded to include:

* Customer feedback collection
* Pending feedback tracking
* Feedback reporting
* Customer rating analysis
* Rule-based sentiment classification
* Issue detection
* A Client Feedback Intelligence Report
* Dashboard-style reporting

This development reflects how a basic data application can gradually grow into a more useful business intelligence tool.

## Current Status

* This project is a learning project.
* The café and its data are fictional.
* The JSON file acts as the main data source.
* DuckDB is used to query and analyse the JSON data.
* The app runs locally using Flask.
* The app has been developed and tested locally.
* Public deployment has not yet been completed.
* The sentiment analysis is rule-based.
* No pretrained sentiment classifier is currently used.
* The project should not be used as a real café point-of-sale, accounting, or production AI system.

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

Make sure the commands are run from inside the project folder.

For example:

```bash
cd curious-bear-cafe
```

Then install the dependencies and run the app.

## Credits

This project was inspired by my learning from the book *DuckDB Up & Running* by my teacher, Mr. Go Figure Out.

The project specifically references learning concepts from:

* Chapter 6: Using DuckDB with JSON files
* Chapter 7: Visualization

The customer feedback intelligence upgrade was developed as part of my continued learning in Python, text analysis, and sentiment analysis.

The project was further modified and extended for my own learning, including creating a café ordering flow, JSON data storage, DuckDB-powered reports, customer feedback tracking, boss notes, dashboard-style analysis, rule-based sentiment classification, and issue detection.

## Author

Created by Michelle.

## Special Thanks

My human teacher, Mr. Go Figure Out, for his encouragement.

My AI teacher, ChatGPT, for guidance.

Curious Bear, for being the café boss and making the learning journey more fun.
