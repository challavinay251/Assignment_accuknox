Social Network API
This is a Django Rest Framework-based social networking API that supports user registration, login, friend requests, and more.

Features
User Registration and Login
Search for users by email or name
Send, accept, and reject friend requests
List friends and pending friend requests
Token-based authentication
Prerequisites
Python 3.8+
Docker (for containerization)
Git (to clone the repository)
Installation Steps
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/socialnetwork.git
cd socialnetwork
Create a virtual environment and activate it:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Apply database migrations:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Create a superuser to access Django admin:

bash
Copy code
python manage.py createsuperuser
Follow the prompts to create your superuser.

Run the development server:

bash
Copy code
python manage.py runserver
Access the API:

Open your browser and go to http://127.0.0.1:8000/.

