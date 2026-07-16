employees = {}

while True:
    print("\nEmployee CRUD Operations")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        salary = input("Enter Salary: ")
        employees[emp_id] = {"Name": name, "Salary": salary}
        print("Employee Added Successfully.")

    elif choice == "2":
        if employees:
            print("\nEmployee Details:")
            for emp_id, details in employees.items():
                print(f"ID: {emp_id}, Name: {details['Name']}, Salary: {details['Salary']}")
        else:
            print("No employee records found.")

    elif choice == "3":
        emp_id = input("Enter Employee ID to Update: ")
        if emp_id in employees:
            name = input("Enter New Name: ")
            salary = input("Enter New Salary: ")
            employees[emp_id] = {"Name": name, "Salary": salary}
            print("Employee Updated Successfully.")
        else:
            print("Employee Not Found.")

    elif choice == "4":
        emp_id = input("Enter Employee ID to Delete: ")
        if emp_id in employees:
            del employees[emp_id]
            print("Employee Deleted Successfully.")
        else:
            print("Employee Not Found.")

    elif choice == "5":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice.")