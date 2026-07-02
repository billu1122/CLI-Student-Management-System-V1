from input_calculation_logic import *

class classroom:
     def __init__(self):
        while True:
            try:
                self.student_class=int(input(f"Enter the class of the students you want to manage: "))
                break
            except ValueError:
                print("invalid Input! Please enter valid Class.")

        self.student_class_section=input(f"Enter class section of the student you wanna mannage : ").strip().upper()
        

        
def add_data_logic():

    my_room = classroom()
    while True:
        try:
            no_student=int(input(f"Enter the number of students you want to enroll in Class {my_room.student_class}-{my_room.student_class_section}:"))
            break
        except ValueError:
            print("Invalid Input! Please enter integer value!")
        
    
    for students in range(no_student):
        print(f"\n--- Entering Data for Student {students + 1} ---")
        student_enter_data(students,students_list,my_room)


def view_data_logic():
    if not students_list:
        print("You have no student data!")

    else: 
        user_choice=user_choice_logic()
        if user_choice==1:
            view_whole_data(students_list)

        elif user_choice==2:
            view_individual_data(students_list)

        else:
            print("Invalid input! please enter valid choice.")


def delete_data_logic():
    if not students_list:
        print("You have no student data!")
    else:
        user_choice=user_choice_logic()
        if user_choice==1:
            delete_Whole_data(students_list)
        elif user_choice==2:
            delete_individual_data(students_list)
        else:
            print("Invalid Input! Please enter valid choice")

def edit_data_logic():
    if not students_list:
        print("You have no student data!")

    else:
        edit_individual_data(students_list)