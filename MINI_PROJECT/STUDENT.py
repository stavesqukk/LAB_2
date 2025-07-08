print("\t\t\t\t\t\tWELCOME TO STUDENT REPORT CARD MANAGEMENT SYSTEM\t\t\t\t\t")
print("CHOOSE THE WORK YOU WANT OR RATHER HAVE TO DO TODAY: ")

names = []
roll_numbers = []
subjects = ["Electric Circuit", "Electronic Circuit", "Python"]
marks = []  # Each element is a list of marks for a student (in subject order)

while True:
    print("\n1. Add new student records (name, roll number, subject-wise marks)")
    print("2. View the report of all students.")
    print("3. Display the topper(s) of the class based on average marks")
    print("4. Search for a student by roll number")
    print("5. Display all students who have failed in one or more subjects.")
    print("6. Optionally update marks of any student.")
    print("7. Show total number of students in the class.")
    print("0. Exit")
    try:
        choice = int(input("Enter the choice you want to continue with: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        name = input("Enter student name: ").strip()
        while True:
            try:
                roll = int(input("Enter roll number: "))
                if roll in roll_numbers:
                    print("Roll number already exists. Please enter a unique roll number.")
                else:
                    break
            except ValueError:
                print("Please enter a valid roll number.")
        print("Subjects available:")
        for i in range(len(subjects)):
            print(str(i+1) + ". " + subjects[i])
        student_marks = []
        for i in range(len(subjects)):
            while True:
                try:
                    m = int(input("Enter marks for " + subjects[i] + " (out of 100): "))
                    if 0 <= m <= 100:
                        student_marks.append(m)
                        break
                    else:
                        print("Marks should be between 0 and 100.")
                except ValueError:
                    print("Please enter a valid number.")
        names.append(name)
        roll_numbers.append(roll)
        marks.append(student_marks)
        print("Student record added successfully.")

    elif choice == 2:
        if len(names) == 0:
            print("No student records to display.")
        else:
            print("\nSTUDENT REPORTS:")
            for i in range(len(names)):
                print("\nName:", names[i])
                print("Roll Number:", roll_numbers[i])
                for j in range(len(subjects)):
                    print(subjects[j] + ":", marks[i][j])
                avg = (marks[i][0] + marks[i][1] + marks[i][2]) / 3
                print("Average:", round(avg, 2))

    elif choice == 3:
        if len(names) == 0:
            print("No student records to check for topper.")
        else:
            max_avg = -1
            topper_index = -1

            for i in range(len(names)):
                avg = (marks[i][0] + marks[i][1] + marks[i][2]) / 3
                if avg > max_avg:
                    max_avg = avg
                    topper_index = i

            print("\nTopper:")
            print(names[topper_index], "(Roll No:", roll_numbers[topper_index], ") with average", round(max_avg, 2))


    elif choice == 4:
        try:
            search_roll = int(input("Enter roll number to search: "))
        except ValueError:
            print("Please enter a valid roll number.")
            continue
        found = False
        for i in range(len(roll_numbers)):
            if roll_numbers[i] == search_roll:
                print("\nName:", names[i])
                print("Roll Number:", roll_numbers[i])
                for j in range(len(subjects)):
                    print(subjects[j] + ":", marks[i][j])
                avg = (marks[i][0] + marks[i][1] + marks[i][2]) / 3
                print("Average:", round(avg, 2))
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == 5:
        found = False
        for i in range(len(names)):
            fail_count = 0
            for j in range(len(subjects)):
                if marks[i][j] < 33:
                    fail_count += 1
            if fail_count > 0:
                found = True
                print(names[i], "(Roll No:", roll_numbers[i], ") failed in", fail_count, "subject(s).")
        if not found:
            print("No student has failed in any subject.")

    elif choice == 6:
        try:
            update_roll = int(input("Enter roll number of student to update marks: "))
        except ValueError:
            print("Please enter a valid roll number.")
            continue
        found = False
        for i in range(len(roll_numbers)):
            if roll_numbers[i] == update_roll:
                print("Current marks for", names[i], ":")
                for j in range(len(subjects)):
                    print(str(j+1) + ". " + subjects[j] + ":", marks[i][j])
                try:
                    sub_choice = int(input("Enter subject number to update (1/2/3): "))
                    if 1 <= sub_choice <= 3:
                        new_mark = int(input("Enter new marks for " + subjects[sub_choice-1] + " (out of 100): "))
                        if 0 <= new_mark <= 100:
                            marks[i][sub_choice-1] = new_mark
                            print("Marks updated successfully.")
                        else:
                            print("Marks should be between 0 and 100.")
                    else:
                        print("Invalid subject number.")
                except ValueError:
                    print("Please enter a valid number.")
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == 7:
        print("Total number of students in the class:", len(names))

    elif choice == 0:
        print("Exiting the system. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")