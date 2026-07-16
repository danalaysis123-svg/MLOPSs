from employee import (
    create_table,
    create_employee,
    delete_employee,
    update_employee,
    view_employee
)

create_table()

while True:

    print("\n========== Employee Management System ==========")
    print("1. CREATE")
    print("2. DELETE")
    print("3. UPDATE")
    print("4. DISPLAY")
    print("5. EXIT")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            create_employee()

        case 2:
            delete_employee()

        case 3:
            update_employee()

        case 4:
            view_employee()

        case 5:
            print("Thank You")
            break

        case _:
            print("Invalid Choice")
