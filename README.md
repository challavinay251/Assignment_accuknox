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

Using Docker
Build and run the Docker containers:

bash
Copy code
docker-compose up --build
Run migrations inside the Docker container:

bash
Copy code
docker-compose run web python manage.py migrate
Create a superuser inside the Docker container:

bash
Copy code
docker-compose run web python manage.py createsuperuser
Access the API and Django Admin:

API: http://127.0.0.1:8000/
Django Admin: http://127.0.0.1:8000/admin/
Postman Collection
You can test all API endpoints using the provided Postman collection. Import the socialnetwork.postman_collection.json file into Postman for quick access to all endpoints.



Contributing
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit them (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.
Contact
For any questions or inquiries, please reach out to challavinay251@gmail.com
