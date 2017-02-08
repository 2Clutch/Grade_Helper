teacher = {"Doe":"0@1!2"}

# grades were assigned using a random number generator
studentDatabase = {"Andrea": [96, 88, 99],
                   "Alex": [86, 92, 78],
                   "Jericka": [72, 74, 75],
                   "Qri": [88, 82, 78],
                   "Alaysia":[73, 72, 72]}

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
        print("1")

    elif decision == "2":
        print("2")

    elif decision == "3":
        print("3")

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
