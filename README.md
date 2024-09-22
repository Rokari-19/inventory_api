

# Inventory API

This is an Inventory Management API built with Django Rest Framework (DRF). The API supports managing **Items** and **Suppliers**, where:
- An **Item** can have multiple **Suppliers**.
- A **Supplier** can deliver multiple **Items**.

## Features
- CRUD operations for Items and Suppliers.
- Swagger API documentation.
- CORS support for allowing all hosts and origins.

## Prerequisites

Ensure you have the following installed:
- Python 3.8+
- pip (Python package installer)
- Virtual environment tools (`venv` for Windows/macOS/Linux)

## Setup Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/inventory-api.git
cd inventory-api
```

### Step 2: Create a Virtual Environment

#### On macOS/Linux:

```bash
python3 -m venv env
source env/bin/activate
```

#### On Windows:

```bash
python -m venv env
.\env\Scripts\activate
```

### Step 3: Install Dependencies

After activating the virtual environment, install the dependencies from `requirements.txt`.

```bash
pip install -r requirements.txt
```

### Step 4: Database Setup

Run the following commands to apply the migrations and set up the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create a Superuser (Optional, for Admin Access)

To access the Django admin interface, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up the superuser account.

### Step 6: Running the Server

Finally, start the Django development server:

```bash
python manage.py runserver
```

The API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### Step 7: Accessing Swagger Documentation

The auto-generated Swagger documentation for the API can be accessed at:

```bash
http://127.0.0.1:8000/api/v1/swagger/
```

You can also view the Redoc documentation at:

```bash
http://127.0.0.1:8000/api/v1/redoc/
```

## Important Files

- `models.py`: Contains the database models for Items and Suppliers.
- `serializers.py`: Defines the serializers for handling API input/output.
- `views.py`: Contains the views for handling API requests.
- `urls.py`: URL routing configuration, including Swagger documentation endpoints.

## CORS Setup (configured by default)

To allow all hosts and origins (useful for public APIs), ensure the following settings in your `settings.py`:

```python
ALLOWED_HOSTS = ['*']

CORS_ALLOW_ALL_ORIGINS = True
```

 `django-cors-headers` is installed and added to `INSTALLED_APPS` and `MIDDLEWARE` in `settings.py` by default.

---