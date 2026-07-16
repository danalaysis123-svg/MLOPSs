import pandas as pd

file_path = r"C:\Users\Student\PyCharmMiscProject\day1\employee.csv"

emp_df = pd.read_csv("employee.csv")

num_employees = len(emp_df)
print(f"Found {num_employees} employees in employee.csv.")

experience_list = []

for i in range(num_employees):
    exp = int(input(f"Enter years of experience for Employee row {i + 1}: "))
    experience_list.append(exp)

emp_df["Experience"] = experience_list

emp_df.to_csv(file_path, index=False)

print("✔ employee.csv updated successfully.\n")

# ---------- Step 2: Create Student Dataset ----------
print("--- Step 2: Create Student Dataset ---")

num_students = int(input("How many student records do you want to add? "))

student_ids = []
student_names = []
grades = []

for i in range(num_students):
    print(f"\nEntering details for Student {i + 1}")

    s_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    grade = input("Enter Grade: ")

    student_ids.append(s_id)
    student_names.append(name)
    grades.append(grade)

student_data = {
    "Student_ID": student_ids,
    "Student_Name": student_names,
    "Grade": grades
}

stu_df = pd.DataFrame(student_data)

student_path = r"C:\Users\Student\PycharmProjects\PythonProject3\Day2\student.csv"

stu_df.to_csv(student_path, index=False)

print("✔ student.csv created successfully.\n")

# ---------- Step 3: Combine Datasets ----------
print("--- Step 3: Combining Datasets ---")

predict_monitor = pd.concat([emp_df, stu_df], axis=1)

monitor_path = r"C:\Users\Student\PycharmProjects\PythonProject3\Day2\predict_monitor.csv"

predict_monitor.to_csv(monitor_path, index=False)

print("✔ predict_monitor.csv generated successfully!")

# ---------- Final Preview ----------
print("\n--- Final Table Preview ---")
print(predict_monitor)