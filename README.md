# Intro to Database (MySQL + Python)

This project demonstrates basic database operations using MySQL and Python. It includes a SQL schema for a simple book store and a Python script for interacting with the database.

## 📁 Files

### 1. `alx_book_store.sql`

This SQL file contains the schema definition for a book store database. It includes the following tables:

- `Authors`
- `Books`
- `Customers`
- `Orders`
- `Order_Details`

Each table is created with appropriate primary keys, foreign keys, and constraints.

### 2. `db_operations.py`

This Python script uses the `mysql-connector-python` library to:

- Connect to the `alx_book_store` MySQL database
- Create a `customers` table (if not already created)
- Insert sample customer records
- Read all customers
- Update a customer's email
- Delete a customer record
- Close the database connection

## 💡 Prerequisites

- Python 3.x
- MySQL server installed and running
- `mysql-connector-python` library installed

Install MySQL connector:

```bash
pip install mysql-connector-python

