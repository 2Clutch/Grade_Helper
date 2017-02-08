teacher = {"Doe":"0@1!2"}

# grades were assigned using a random number generator
studentDatabase = {"Andrea": [96, 88, 99],
                   "Alexandra": [86, 92, 78],
                   "Jericka": [72, 74, 75],
                   "Qri": [88, 82, 78],
                   "Alaysia":[73, 72, 72]}

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
        del studentDatabase[nameToRemove]

    else:
        print("Student does not exist.")

    print(studentDatabase)

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
        print("3")

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
