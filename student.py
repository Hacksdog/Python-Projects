# 2. STUDENT GRADE MANAGEMENT SYSTEM
# --------------------------------------------------
# Concepts: List, Dictionary, Loops, Functions
# Description:
# - Allow the user to add student names, subjects, and marks.
# - Calculate total, average, and highest scorer.
# - Store each student’s record in a dictionary.
# - Display class average and topper.

def collect_student_data():
    students = [] 

    while True:
        student_name = input("Enter the student name: ").title()
        subject = input("Enter the subject: ").title()
        student_number = int(input("Enter Number: "))

        student_info = {
            "name": student_name,
            "subject": subject,
            "number": student_number
        }

        students.append(student_info)

        know = input("Want to enter any other student details? 'y' for Yes 'n' for No: ").lower()
        if know == 'n':
            
            break

    return students  



all_students = collect_student_data()

count = len(all_students)


total = 0
highest = 0
topper = ''
for student in all_students:
    total+= student["number"]
    if highest<student["number"]:
        highest = student["number"]
        topper = student["name"]

avg = total/count
print(f'Total Number is : {total}')
print(f'Class Avarage is : {avg}')
print(f'Hight Score is : {highest}')
print(f'class topper is : {topper}')
print(f'Your final Dict Is\n{all_students}')





        
                

   
