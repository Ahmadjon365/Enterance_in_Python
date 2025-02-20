import sqlite3
from contextlib import closing

database_path = "sample-database (5).db"


def get_connection(database_path):
    return closing(sqlite3.connect(database_path))


def get_employee(database_path, employee_id):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM employees WHERE employee_id=?", (employee_id,))
        return cursor.fetchone()


def create_employee(database_path, first_name, last_name, email):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO employees (first_name, last_name,email) VALUES (?, ?,?)",
                       (first_name, last_name, email))
        connection.commit()
        return cursor.lastrowid


emp_id = create_employee(database_path, "Akmal", "Tohirov", "akmal@mail.ru")
print(emp_id)
