# Django Framework Project

This is a simple Django-based web application designed to demonstrate core functionalities of the Django framework.

---

## Features
- **Django Framework**: Built using Django, a high-level Python web framework.
- **Database Support**: Integrated with a relational database (e.g., SQLite, PostgreSQL, or MySQL).
- **Modular Architecture**: Easily extendable for adding more features.

---

## Prerequisites
Before running this project, ensure you have the following installed on your system:
- **Python**: Version 3.8 or higher
- **pip**: Python's package installer
- **virtualenv** (recommended): For isolating the project's dependencies

---

## Installation and Setup

### Step 1: Clone the Repository
Clone this repository and navigate to the project directory:
```bash
git clone [https://github.com/yourusername/your-repository.git](https://github.com/ANTHONY8652/skillaid-connect-API.git)
cd skillaid-connect-API

### Step 2: Install Depedencies

Install the required Python packages:
```bash
pip install -r requirements.txt

###Step 3: Create a Superuser
Create a superuser:
```bash
python manage.py createsuperuser

### Step 4: Run Migrations
Create an admin user for the Django admin interface:
```bash 
python manage.py makemigrations
python manage.py migrate

###Step 5: Run the Development Server
Start the django development server
```bash
python manage.py runserver

###Step 6: Start the local development server
Go to this address to access the server
http://localhost:8000

###Step 7: Land on the landing page
Here you will find a drf-yasg swagger with ui
There is a list of all the endpoints listed here together with their respective urls

Have fun

