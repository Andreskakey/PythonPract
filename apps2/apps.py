"""student = {"name": "Jose",
           "mark": [70, 50, 80, 44, 99],
           "exam" : {
               "final" : 70,
               "midterm" : 50
           }}
print(student["exam"]["final"])
"""
student_list= []

class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []
    def avg_mark (self)
        number = len(self.marks)
        if number == 0:
            return 0

            # add all of the student mark
        total = sum(self.marks)
        return total / number

def create_student():
    #ask user name
    #create the dictionary
    #return dictionary
    name = input("Enter new student name: ")
    student_data = Student(name)
    """
    student_data = {
        'name': name,
        'mark': []
    }
    """
    return student_data

#my_list = []
#print(my_list.append(5))
#print(my_list)
#print(create_student())

#s = create_student()

def add_mark(student, mark):
    #append a mark to the student dictionary
    student.marks.append(mark)
   # return None
"""
def Calc_avg_mark(student):
    #Divide them by the total numbers of mark
    number = len(student.marks)
    if number == 0:
        return 0

        # add all of the student mark
    total = sum(student.marks)
    return total/number
#add_mark(s, 5) # passing by reference
"""
"""
s =create_student()

print (Calc_avg_mark(s))
add_mark(s,5)
print (Calc_avg_mark(s))
add_mark(s,10)
print (Calc_avg_mark(s))
"""
def print_student_details(student):
    #print out a string about the information of the student
    print("{}, average mark: {}.".format(student.name,
                                         student.avg_mark()))

def print_student_list(students):
    for i, student in enumerate(students):
        print("ID: {}".format(i))
        print_student_details(student)

def menu():
    #add a student to student list
    #add a mark to a student
    #print a lis of student
    #exitl the app
    selection = input("enter 'p ' to print the student list, "
                       "'s' to add new student, "
                       "'a' to add a mark to a student, or "
                       "'q' to quit " 
                        "Enter Your Selection : ")
    while selection != 'q':
        if selection == 'p':
            print_student_list(student_list)
        elif selection == 's':
            student_list.append(create_student())
        elif selection == 'a':
            student_id = int(input("Enter the student ID to add a mark to: "))
            student = student_list[student_id]
            new_mark = int(input("enter the new mark to be added: "))
            add_mark(student, new_mark)

        selection = input("enter 'p ' to print the student list, "
                       "'s' to add new student, "
                       "'a' to add a mark to a student, or "
                       "'q' to quit " 
                        "Enter Your Selection : ")

menu()