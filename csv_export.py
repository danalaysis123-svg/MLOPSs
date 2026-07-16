
import csv
import employee
def csv_convert():
    print("csv export started...")
    employees = employee.read_employee()
    if employees is None:
        print("No employee data found ")
        return
    if len(employees)==0:
        print("No employee data found ")
        return
    with open('employees.csv', 'w', newline='',encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
        "Employee ID",
        "Employee Name",
        "Department",
        "Employee Salary"
        ])
        for emp in employees:
            writer.writerow([
                emp[0],
                emp[1],
                emp[2],
                emp[3]
            ])
print("Employee data sucessfully exported")