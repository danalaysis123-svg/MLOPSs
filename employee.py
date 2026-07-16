from sql import execute_query


def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS employee(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        department INTEGER,
        salary REAL
    )
    """
    execute_query(query)


def get_int_input(prompt):
    """Helper function to safely get an integer input."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(" Invalid input! Please enter a whole number.")


def get_float_input(prompt):
    """Helper function to safely get a float (decimal) input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(" Invalid input! Please enter a valid decimal or number.")


def create_employee():
    n = get_int_input("Enter the number of employees: ")

    for i in range(n):
        print(f"\n--- Adding Employee {i + 1} ---")
        emp_id = get_int_input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        department = input("Enter Department: ")
        salary = get_float_input("Enter Employee Salary: ")

        query = """
        INSERT INTO employee(id, name, department, salary)
        VALUES(?, ?, ?, ?)
        """

        result = execute_query(query, (emp_id, name, department, salary))

        if result:
            print("Employee Added Successfully")
        else:
            print("Failed to add employee")


def delete_employee():
    view_employee()

    emp_id = get_int_input("\nEnter Employee ID to delete: ")

    query = "DELETE FROM employee WHERE id=?"
    result = execute_query(query, (emp_id,))

    if result:
        print("Employee Deleted Successfully")
    else:
        print("Employee Not Found")


def update_employee():
    view_employee()

    emp_id = get_int_input("\nEnter Employee ID to Update: ")

    name = input("Enter New Name: ")
    department = input("Enter New Department: ")
    salary = get_float_input("Enter New Salary: ")

    query = """
    UPDATE employee
    SET
        name=?,
        department=?,
        salary=?
    WHERE id=?
    """

    result = execute_query(query, (name, department, salary, emp_id))

    if result:
        print("Employee Updated Successfully")
    else:
        print("Employee Not Found")


def view_employee():
    query = "SELECT * FROM employee"
    rows = execute_query(query)

    if rows is None or len(rows) == 0:
        print("\nNo employees found.")
        return

    print("\n========== Employee Details ==========")
    for row in rows:
        print()
        print("Employee ID   :", row[0])
        print("Name          :", row[1])
        print("Department    :", row[2])
        print("Salary        :", row[3])