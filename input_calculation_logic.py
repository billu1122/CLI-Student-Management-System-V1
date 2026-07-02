unique_user_id=1
students_list={}

def calculation_logic(marks):
    total_marks = sum(marks)
    percentage = total_marks * 100 / 500
    return total_marks,percentage


def marks_input_logic(subjects,marks,student_name):
    for sub in subjects:
        while True:
            try:
                m = int(input(f"Enter Student {student_name} {sub} Marks: "))
            except ValueError:
                print("Invalid Input Please integer value")
                continue
            if m <= 100 and m>=0:
                marks.append(m)
                break
            else:
                print("Marks Can't Be More/less Than 100")


def marks_calculator_logic(student_name):
    subjects = ["Physics", "Chemistry", "Maths", "Computer Science", "English"]
    marks=[]
    
    marks_input_logic(subjects,marks,student_name)
    final_marks, final_percentage=calculation_logic(marks)
    return final_marks,final_percentage, subjects, marks


def student_enter_data(students,students_list,my_room):
        student_name=input(f"Enter name of Student {students+1}: ").strip()

        while True:
            try:
                student_roll_no=int(input(f"Enter Roll no. of student {student_name} : "))
                break
            except ValueError:
                    print("invalid Input! Please enter valid Roll no.")
                    continue
        while True:
            try:
                student_admit_no=int(input(f"Enter Admission no. of student {student_name} :"))
                string_admit_no=str(student_admit_no)
                unique_user_id="user_"+string_admit_no

                if unique_user_id in students_list:
                 print("Admission No. Already Exists! Please try again.")
                 continue
                else:
                    break
            except ValueError:
                 print("invalid Input! Please enter valid Admission nol no.")
                 continue
             

        final_marks, final_percentage,_, mark=marks_calculator_logic(student_name)

        
        student_data = {
        "Name": student_name,
        "Admission no.": student_admit_no,
        "Roll no": student_roll_no,
        "Class": my_room.student_class,
        "Section": my_room.student_class_section,
        "Physics": mark[0],
        "Chemistry": mark[1],
        "Maths" :mark[2],
        "Computer Science": mark[3],
        "English": mark[4],
        "Total Marks": final_marks,
        "Total Percentage": final_percentage
    }
        students_list[unique_user_id] = student_data
        return students_list,final_marks,final_percentage


def user_choice_logic():
    while True:
        print("1. For whole class")
        print("2. For individual ")
        try:
            user_choose=int(input("Enter your choice: "))
            return user_choose
        except ValueError:
            print("Invalid Input! Please enter valid choice.")


def view_individual_data(students_list, purpose="view"):
    while True:
        try:
            student_admit_no = input(f"Enter Admission no. of student data you wanna {purpose} (or enter 'EXIT' to exit): ").strip()
            
            if student_admit_no.upper() == "EXIT":
                print(f"Successfully exited the individual {purpose} menu!")
                return None
                
            unique_user_id = "user_" + student_admit_no

            if unique_user_id in students_list:
                individual_data = students_list.get(unique_user_id)
                print(f"\n--- The data of student {individual_data.get('Name')} is below ---")   
                
                for key, value in individual_data.items():
                    print(f"{key}:{value}")
                return unique_user_id
            else:
                print(f"Student with Admission no. '{student_admit_no}' does not exist in database.")
                continue            
        except Exception as e:
            print("Something went wrong! Please enter a valid Admission no.")


def view_whole_data(students_list):
    for students in students_list:
        individual_data=students_list.get(students)
        print(f"\n--- The data of student {individual_data.get('Name')} is below ---")   
        for key,value in individual_data.items():
            print(f"{key}:{value}")


def delete_Whole_data(students_list):
    view_whole_data(students_list)
    print("-" * 50)
    print("WARNING: You are about to DELETE ALL STUDENT DATA.")
    print("This action is permanent and cannot be undone.")
    print("-" * 50)
    while True:
        confirmation=input("WARNING: Are you sure you want to proceed? Type 'DELETE' to confirm all data erasure, or type 'EXIT' to cancel: ")
        if confirmation=="DELETE":
            students_list.clear()
            print("All student data is successfully deleted")
            break
        elif confirmation=="EXIT":
            print("Deleting data process is canceled!")
            break
        else:
            print("Invalid input! Please type 'DELETE' to erase or 'EXIT' to cancel (entries are case-sensitive).")
            continue


def delete_individual_data(students_list):
    unique_user_id = view_individual_data(students_list, "Delete")

    if unique_user_id is None:
        return

    student_name = students_list[unique_user_id].get('Name', 'Student')

    print("-" * 50)
    print(f"WARNING: You are about to DELETE student.")
    print("This action is permanent and cannot be undone.")
    print("-" * 50)
    while True:
        confirmation=input(f"WARNING: Are you sure you want to proceed? Type 'DELETE' to confirm  data erasure of student {student_name}, or type 'EXIT' to cancel: ")
        if confirmation=="DELETE":
            students_list.pop(unique_user_id)
            print(f" {student_name} data is successfully deleted")
            break
        elif confirmation=="EXIT":
            print("Deleting data process is canceled!")
            break
        else:
            print("Invalid input! Please type 'DELETE' to erase or 'EXIT' to cancel (entries are case-sensitive).")
            continue


def edit_individual_data(students_list,subjects = ["Physics", "Chemistry", "Maths", "Computer Science", "English"]):
    unique_user_id= view_individual_data(students_list, "Edit")



    if unique_user_id is None:
        return
    
    student_name = students_list[unique_user_id].get('Name','Student')
    
    while True:
        print("Available Editable fields:-")
        print("- Name")
        print("- Roll no")
        print("- Class")
        print("- Section")
        print("- Subject Marks")
        print("- Exit")

        edit_choice=input(f"Enter the field name exactly as shown to edit profile of {student_name}:").capitalize().strip()


        if edit_choice in ['Name', 'Roll no', 'Class', 'Section']:
            new_data=input(f"Enter the new {edit_choice} for {student_name} :").capitalize().strip()
            print(f"You Have successfully edited {students_list[unique_user_id].get(edit_choice)} into {new_data}.")
            students_list[unique_user_id].update({edit_choice:new_data})
            return unique_user_id,students_list
        
        elif edit_choice in ['Subject','Subject marks','Marks','Subject mark','Subjects mark',"Subjects","Subjects marks"]:

            print("Available Editable fields:-")
            print("- Physics")
            print("- Chemistry")
            print("- Maths")
            print("- Computer Science")
            print("- English")

            edit_subject=input(f"Enter the subject name exactly as shown to edit profile of {student_name:}").strip().capitalize()

            for subject in subjects:
            
                if subject==edit_subject:
                    try:
                        m = int(input(f"Enter Student {student_name} {subject} Marks: "))
                    except ValueError:
                        print("Invalid Input Please integer value")
                        continue
                    if m <= 100 and m>=0:
                        students_list[unique_user_id][subject]=m
                        current_marks=[]

                        for sub in subjects:
                            current_marks.append(students_list[unique_user_id][sub])
                            
                            total_marks, percentage = calculation_logic(current_marks)
                            
                            students_list[unique_user_id]["Total Marks"] = total_marks
                            students_list[unique_user_id]["Total Percentage"] = percentage
                            
                            print(f"Successfully updated {subject} marks and recalculated totals.")
                            return unique_user_id, students_list

                    else:
                        print("Marks Can't Be More/less Than 100")

        elif edit_choice== "Exit":
            print(f"The process to Edit profile of {student_name} is canceled successfully! ")
            break

        else:
            print("Invalid Input! Please enter correct choice (Make sure capatilization and spelling is same as menu)")