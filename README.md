To-Do App (Python (Flask) + PostgreSQL)

A simple, full-stack To-Do List web application built with Flask and PostgreSQL. This app allows users to create, update, and delete tasks, offering a minimal and clean interface for task management.

Features
•	Add new tasks with a description
•	Mark tasks as complete or incomplete
•	Edit task content
•	Delete tasks
•	Responsive UI
•	Persistent storage with PostgreSQL
•	Clean modular Flask structure
Tech Stack
Frontend	HTML, CSS, JavaScript (Vanilla)
Backend	Python (Flask)
Database	PostgreSQL

Setup & Installation
1. Clone the Repository
git clone https://github.com/msamiram/todo-python.git
cd todo-python
2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Configure Environment Variables
Create a .env file in the root directory and add your PostgreSQL URI:
DATABASE_URL=postgresql://username:password@localhost:5432/tododb
FLASK_ENV=development
SECRET_KEY=your_secret_key_here
5. Initialize the Database
Ensure PostgreSQL is running and the tododb database is created.
psql -U your_user
CREATE DATABASE tododb;
Then initialize tables:
flask db init
flask db migrate
flask db upgrade
6. Run the App
flask run
The app will be available at http://localhost:5000.

Example Usage
•	Open your browser at localhost:5000
•	Add a task  
•	Mark it as done(in progress or complete) or delete it
•	Filter tasks by their ststus
•	Tasks are stored persistently in the PostgreSQL database

