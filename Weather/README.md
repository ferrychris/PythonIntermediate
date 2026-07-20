# Python SQLite Projects

This repository contains beginner-friendly Python scripts to help you learn and practice interacting with SQLite databases using Python. It covers the core concepts of creating tables, inserting data, reading data, updating records, and deleting them (CRUD operations).

## Projects Included

### 1. Weather Data Fetcher (`app.py`)
Despite being in the "Crypto" folder, this script connects to the XWeather API to fetch real-time weather conditions for New York, NY, and stores that data in a local database.

**Features:**
- Makes HTTP requests to an external API using the `requests` library.
- Parses complex JSON data.
- Connects to an SQLite database (`crypto.db`).
- Creates a `weather_conditions` table if it doesn't exist.
- Performs full CRUD operations:
  - **Create:** Inserts the fetched weather data.
  - **Read:** Selects and prints the records.
  - **Update:** Updates the temperature for New York.
  - **Delete:** Deletes the record for New York.

### 2. Students Database (`text.py`)
A simple script demonstrating how to create and manage a database for storing student information.

**Features:**
- Connects to an SQLite database (`student.db`).
- Creates a `students` table with columns for `id`, `name`, `age`, `course`, and `cgpa`.
- Inserts a new student record into the database.
- Selects and prints the existing records.

## Prerequisites

Before running these scripts, ensure you have Python installed. You will also need to install the `requests` library for `app.py` to work correctly.

You can install it using pip:
```bash
pip install requests
```

## How to Run

Navigate to the project folder in your terminal and run the scripts using Python:

**To run the weather app:**
```bash
python app.py
```

**To run the students app:**
```bash
python text.py
```

## Key Learnings
- Proper SQL syntax for SQLite.
- Handling database connections (`conn.connect()`, `conn.commit()`, `conn.close()`).
- Utilizing cursors (`cursor.execute()`, `cursor.fetchall()`).
- Navigating nested JSON dictionaries and lists from API responses.
