# FastAPI Student Management System

Welcome to the FastAPI Student Management System! This project provides a RESTful API built with FastAPI for managing students and mentors, along with a MySQL database to store the data. The system also includes basic CRUD operations for both students and mentors.

## Features

- **Create, Read, Update, Delete (CRUD) Operations:** Perform CRUD operations for both students and mentors via the provided API endpoints.
- **Data Validation:** Input data is validated using Pydantic schemas to ensure consistency and integrity.
- **Cross-Origin Resource Sharing (CORS):** CORS middleware is enabled to allow cross-origin requests, making it easy to integrate with frontend applications.
- **MySQL Database:** Utilizes MySQL database to persist mentor and student data.
- **Error Handling:** Proper error handling is implemented for various scenarios, ensuring robustness and reliability of the system.
- **Scalability:** FastAPI's asynchronous capabilities make the system highly scalable, capable of handling large numbers of concurrent requests efficiently.

## Technologies Used

- **FastAPI:** FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **SQLAlchemy:** SQLAlchemy is used as the ORM (Object-Relational Mapping) library to interact with the MySQL database.
- **Pydantic:** Pydantic is used for data validation and serialization/deserialization of input and output data.
- **MySQL:** MySQL is used as the relational database management system for storing mentor and student data.
- **Python 3:** The project is written in Python 3, leveraging its powerful features and libraries.
- **CORS Middleware:** FastAPI's built-in CORS middleware is used to handle Cross-Origin Resource Sharing.

## Database Structure

The MySQL database structure for this project includes two tables: `mentors` and `students`.

### Mentors Table

| Column   | Data Type   | Description                |
|----------|-------------|----------------------------|
| empid    | VARCHAR(14) | Primary key - Employee ID |
| name     | VARCHAR(50) | Mentor's name             |
| desig    | VARCHAR(20) | Mentor's designation      |
| email    | VARCHAR(50) | Mentor's email address    |
| ph       | INT         | Mentor's phone number     |
| password | VARCHAR(10) | Mentor's password         |

### Students Table

| Column    | Data Type   | Description                    |
|-----------|-------------|--------------------------------|
| regno     | VARCHAR(14) | Primary key - Registration number |
| name      | VARCHAR(50) | Student's name                 |
| email     | VARCHAR(50) | Student's email address        |
| phone     | INT         | Student's phone number         |
| programme | VARCHAR(100) | Student's program              |
| score     | INT         | Student's score                |
| empid     | VARCHAR(10)  | Foreign key - Mentor's employee ID |

## Getting Started

### Prerequisites

- Python 3.x
- MySQL Server

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/geoseiden/fastapi-student-management.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up MySQL database:
   
   - Create a MySQL database named `cse_app`.
   - Update the database connection URL in `database.py` if necessary.

4. Run the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

5. Access the API documentation at `http://127.0.0.1:8000/docs` in your web browser.

## API Endpoints

- **Mentors:**
  - `GET /mentors`: Get all mentors.
  - `GET /mentors/{empid}`: Get mentor by ID.
  - `POST /mentors`: Create a new mentor.
  - `PUT /mentors/{empid}`: Update an existing mentor.
  - `DELETE /mentors/{empid}`: Delete a mentor.
- **Students:**
  - `GET /students`: Get all students.
  - `GET /students/{regno}`: Get student by registration number.
  - `POST /students`: Create a new student.
  - `PUT /students/{regno}`: Update an existing student.
  - `DELETE /students/{regno}`: Delete a student.
- **Additional Endpoint:**
  - `GET /students/mentor/{empid}`: Get students by mentor ID.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.
