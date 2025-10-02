import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="pythonuser",
    password="yourpassword",
    database="your_database_name"
)
