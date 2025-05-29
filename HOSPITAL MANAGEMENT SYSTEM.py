import mysql.connector
import tkinter as tk
from tkinter import messagebox

# Function to establish a connection to the MySQL database
def create_db_connection():
    """ Establish a connection to the MySQL database. """
    connection = mysql.connector.connect(
        host="localhost",      # Replace with your host (localhost for local MySQL server)
        user="root",           # Replace with your MySQL username
        password="password",   # Replace with your MySQL password
        database="hospital_management_system"
    )
    return connection

# Function to add a new patient
def add_patient():
    """ Add a new patient to the database. """
    connection = create_db_connection()
    cursor = connection.cursor()

    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    gender = input("Enter patient gender (Male/Female): ")
    contact_number = input("Enter patient contact number: ")
    address = input("Enter patient address: ")

    query = """INSERT INTO Patients (name, age, gender, contact_number, address)
               VALUES (%s, %s, %s, %s, %s)"""
    values = (name, age, gender, contact_number, address)

    cursor.execute(query, values)
    connection.commit