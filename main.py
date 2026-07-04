import sys
from student_logic import *
from input_calculation_logic import *

while True:
    print("\n===== Student Management System =====")
    print("1. Enter Student Info")
    print("2. Edit Student Info")
    print("3. Delete Student Info")
    print("4. View Student Info")
    print("5. Review Students Info")
    print("6. Exit Program")

    try:
       choice = int(input("Select an option: "))
    except ValueError:
        print("Invalid input! Please select a  valid choice.")
        continue


    if choice == 1:
        add_data_logic()

    elif choice == 2:
        edit_data_logic()

    elif choice == 3:
        delete_data_logic()

    elif choice == 4:
        view_data_logic()

    elif choice == 5:
        review_whole_logic()

    elif choice == 6:
        print("Exiting program. Goodbye!")
        sys.exit()

    else:
        print("Invalid choice! Please select a valid option.")