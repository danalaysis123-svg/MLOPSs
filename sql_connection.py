import sqlite3

def get_connection():
    try:
        connection = sqlite3.connect("employee.db")
        return connection
    except Exception as e:
        print("Database Connection Failed")
        print(e)
        return None

