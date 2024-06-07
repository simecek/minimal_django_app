# ChipSEQ Experiment Results App

## Introduction

This Django app allows you to store and filter ChipSEQ experiment results. You can filter the results based on protein name, chromosome, and genomic interval, and view the results in a tabular format with pagination.

## Installation

1. **Clone the repository:**
```
   git clone https://github.com/your-repo/chipseq_app.git
   cd chipseq_app
```
2. **Create a virtual environment and activate it:**
```
   python3 -m venv venv
   source venv/bin/activate
```
3. **Install the dependencies:**
```
   pip install -r requirements.txt
```
4. **Apply the migrations:**
```
   python manage.py makemigrations
   python manage.py migrate
```
5. **Create a superuser to access the admin interface:**
```
   python manage.py createsuperuser
```
6. **Run the development server:**
```
   python manage.py runserver
```
7. **Open your browser and go to `http://127.0.0.1:8000` to view the app. You can access the admin interface at `http://127.0.0.1:8000/admin` to add experiment results.

## Usage

- **Filtering Results:**
  - Use the form on the main page to filter results based on protein name, chromosome, and genomic interval.
  - You can specify any subset of the filtering parameters (e.g., just the chromosome) without filling out all fields.

- **Viewing Results:**
  - The results are displayed in a table, showing only the first 50 results by default.
  - Use the pagination controls to navigate through the results.

## Populating the Database with Sample Data

You can populate the database with sample data using a custom management command:
```
   python manage.py populate_data
```
This command will create 100 sample experiment results.

## Dependencies

- **Django**: `>=3.2`
- **django-bootstrap4**: for styling
