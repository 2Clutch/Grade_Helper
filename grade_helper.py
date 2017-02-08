def main():
    print("""

    Welcome to Grade Helper

    [1] - Enter Grades
    [2] - Remove Student
    [3] - Grade Average
    [4] - Exit

    """)

    decision = input("What will you be working on today? (Enter a number): ")

    if decision == "1":
        print("1")

    elif decision == "2":
        print("2")

    elif decision == "3":
        print("3")

    else:
        print("Sorry, but your choice wasn't valid. Please try again.")

while True:
    main()
