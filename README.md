To-Do App (Python (Flask) + PostgreSQL)

A simple, full-stack To-Do List web application built with Flask and PostgreSQL. This app allows users to create, update, and delete tasks, offering a minimal and clean interface for task management.

Features
•	Add new tasks with a description
•	Mark tasks as complete, in progress or new
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
4. Configure Environment Variables
Create a .env file in the root directory and add your PostgreSQL URI:
DATABASE_URL=postgresql://postgres:samira0110@host.docker.internal:5432/todo_db
JWT_SECRET=your-very-secret-key
5.Build and run the containers
docker-compose up --build


Example Usage
•	Open your browser at localhost:5000
•	Add a task  
•	Mark it as done(in progress or complete) or delete it
•	Filter tasks by their ststus
•	Tasks are stored persistently in the PostgreSQL database

