# Task Management APP

This is a Task Management APP built using Django and Django Rest Framework. It allows users to create, update, delete, and manage tasks, as well as assign users to tasks.

## Table of Contents

- [Installation](#installation)
- [Setup](#setup)
- [Running the Project](#running-the-project)
- [API Documentation](#api-documentation)
  - [Sample Requests and Responses](#sample-requests-and-responses)
- [Test Credentials](#test-credentials)
- [Testing the API](#testing-the-api)
- [License](#license)

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- Django 3.x or higher
- Django Rest Framework
- Postman (optional for testing the API)

### Step-by-Step Installation

1. Clone the repository:

   ```bash
   git clone  https://github.com/Rajatb04/TaskManagementApp.git
   cd TaskManagementApp

2. Create and activate a virtual environment:

   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux


3. Install the required dependencies:
    pip install -r requirements.txt


4. Set up environment variables by creating a .env file in the root directory of the project with the following content:
   SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1


5. Apply database migrations:
    python manage.py migrate



6. Create a superuser (for accessing Django Admin and creating users):
python manage.py createsuperuser

Setup
Ensure that the users app is correctly set up. Refer to your users/models.py and ensure the User model is configured correctly.

Add the users app to the INSTALLED_APPS in settings.py:

INSTALLED_APPS = [
    ...
    'users',
    'tasks',
    'rest_framework',
]

Running the Project
To run the development server, use the following command:
python manage.py runserver





API Documentation
1. Create a Task
POST /api/tasks/

 curl --location 'http://localhost:8000/api/tasks/' \
--header 'Content-Type: application/json' \
--data '{
         "name": "Develop Dashboard",
         "description": "Create user dashboard interface",
         "task_type": "DEV",
         "status": "NS",
         "assigned_users": [1]
     }'
     
Request:
{
         "name": "Develop Dashboard",
         "description": "Create user dashboard interface",
         "task_type": "DEV",
         "status": "NS",
         "assigned_users": [1]
     }

     Response:
     {
    "id": 1,
    "name": "Develop Dashboard",
    "description": "Create user dashboard interface",
    "created_at": "2025-03-25T12:49:52.263529Z",
    "completed_at": null,
    "task_type": "DEV",
    "status": "NS",
    "assigned_users": [
        1
    ],
    "assigned_user_details": [
        {
            "id": 1,
            "name": "",
            "email": "test@gmail.com"
        }
    ]
}


2. List All Tasks
GET /api/tasks/

curl --location 'http://localhost:8000/api/tasks/user_tasks/?user_id=1'

Response:

[
    {
        "id": 1,
        "name": "Develop Dashboard",
        "description": "Create user dashboard interface",
        "created_at": "2025-03-25T12:49:52.263529Z",
        "completed_at": null,
        "task_type": "DEV",
        "status": "NS",
        "assigned_users": [
            1
        ],
        "assigned_user_details": [
            {
                "id": 1,
                "name": "",
                "email": "test@gmail.com"
            }
        ]
    }
]


3. Assign a Task
PATCH /api/tasks/1/assign_users/

curl --location --request PATCH 'http://localhost:8000/api/tasks/1/assign_users/' \
--header 'Content-Type: application/json' \
--data '{"user_ids": [1]}'

Request:
{
  "title": "Updated Task",
  "description": "This task has been updated",
  "assigned_users": [1, 2]  # Add more users as needed
}

Response:

{
    "id": 1,
    "name": "Develop Dashboard",
    "description": "Create user dashboard interface",
    "created_at": "2025-03-25T12:49:52.263529Z",
    "completed_at": null,
    "task_type": "DEV",
    "status": "NS",
    "assigned_users": [
        1
    ],
    "assigned_user_details": [
        {
            "id": 1,
            "name": "",
            "email": "test@gmail.com"
        }
    ]
}
     

