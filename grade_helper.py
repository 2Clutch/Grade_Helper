from statistics import mean as m

teacher = {"Doe":"0@1!2"}

# grades were assigned using a random number generator
studentDatabase = {"Andrea": [90, 88, 89],
                   "Alexandra": [95, 75, 79],
                   "Jericka": [92, 79, 81],
                   "Qri": [85, 85, 85],
                   "Alaysia":[96, 74, 100]}

# add option where test grade has to be entered for every student
# if only one student's grade is entered, other automatically get a zero
# add an option allowing teacher to modify grades whenever they would like

def enterGrades():
    nameToEnter = input("Student Name: ")
    gradeToEnter = input("Grade: ")

    if nameToEnter in studentDatabase:
        print("Adding Grade ...")
        studentDatabase[nameToEnter].append(gradeToEnter)

    else:
        print("Student does not exist.")

    print(studentDatabase)

def removeStudent():
    nameToRemove = input("Which student would you like to remove from the database? \n")

    if nameToRemove in studentDatabase:
        print("Removing Student ...")
        print("Please understand this is not reversible. Thank you!")
        del studentDatabase[nameToRemove]

    else:
        print("Student does not exist.")

    print(studentDatabase)

def gradeAverage():
    for student in studentDatabase:
        gradeList = studentDatabase[student]
        avg = m(gradeList)

        print(student, "has a grade average of", avg)

        # throwing error when one student has more grades than others
        # will have to define test case for that scenario
        # gradeAverage should be able to run independently regardless of the other students number of grades

def main():
    print("""
    Welcome to Grade Helper

    [1] - Enter Grades
    [2] - Remove Student
    [3] - Grade Average
    [4] - Exit

    """)

    decision = input("What will you be working on today? (Enter a number): \n")

    if decision == "1":
        enterGrades()

    elif decision == "2":
        removeStudent()

    elif decision == "3":
        gradeAverage()

    elif decision == "4":
        exit()

    else:
        print("Sorry, but your choice wasn't valid. Please try again.")

login = input("Username: ")
passw = input("Password: ")

if login in teacher:

    if teacher[login] == passw:
        print("Welcome,", login)

        while True:
            main()

    else:
        print("Invalid Password. You should try again sometimes.")

else:
    print("Invalid Username. You should never try again! Not now. Not ever!!")
