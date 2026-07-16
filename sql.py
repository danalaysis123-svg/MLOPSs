
from sql_connection import get_connection

def execute_query(query, params=None):
    connection = get_connection()

    if connection is None:
        return None

    cursor = connection.cursor()

    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        if query.strip().upper().startswith("SELECT"):
            result = cursor.fetchall()
        else:
            connection.commit()
            result = cursor.rowcount

        return result

    except Exception as e:
        print("SQL Execution Failed")
        print(e)
        return None

    finally:
        cursor.close()
        connection.close()