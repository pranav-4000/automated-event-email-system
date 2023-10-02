
# Event Email System

Django-based backend API designed to automatically send emails on special occasions such as birthdays and work anniversaries.


## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [API Endpoints](#api-endpoints)
- [Configuration](#configuration)


## Getting Started

### Prerequisites

Before setting up and running the Event Email System, make sure you have the following prerequisites installed:

- Python 3.9
- Django (latest version)
- Django Rest Framework (latest version)
- Additional Python libraries as required (see `requirements.txt`)
- Setup Email and Password in settings.py

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/pranav-4000/automated-event-email-system.git
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

1. Run database migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. Create a superuser for admin access:

   ```bash
   python manage.py createsuperuser
   ```

3. Start the development server:

   ```bash
   python manage.py runserver
   ```

4. Access the admin panel at `http://localhost:8000/admin/` and log in using the superuser credentials.

### API Endpoints

The Event Email System have a swagger API endpoints:

`http://localhost:8000/`

## Configuration

You can configure the Event Email System by modifying the settings in the `settings.py` file. Configure email settings, database settings, and other application-specific configurations here.
