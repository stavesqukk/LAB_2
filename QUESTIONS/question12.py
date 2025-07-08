#12. Create a dictionary to store student names as keys and their scores in three subjects as
#values (in a list). Write functions to:
#a. Display the average marks of each student
#b. Find the topper
#c. Update the marks of a student

students = {}
averages = {}
n = int(input("Enter the number of students: "))
for i in range(n):
    name = input(f"Enter the name of student {i+1}: ")
    name.lower()
    marks = []
    for j in range(3):
        mark = int(input(f"Enter mark of subject {j+1} for {name}  (total marks 100): "))
        marks.append(mark)
    students[name] = marks

print("\nAverage marks of each student:")
for name, marks in students.items():
    avg = sum(marks) / len(marks)
    averages[name] = avg
    print(f"{name}: {avg:.2f}")

topper = max(averages, key=averages.get)
print(f"\nTopper: {topper} with average marks {averages[topper]:.2f}")

update_name = input("\nEnter the name of the student whose marks you want to update: ")

if update_name in students:
    print(f"Current marks for {update_name}: {students[update_name]}")
    while True: 
        subject_no = int(input("Enter the subject number to update (1/2/3): "))
        if 1 <= subject_no <= 3:
            new_mark = int(input(f"Enter new mark for subject {subject_no} (out of 100): "))
            students[update_name][subject_no - 1] = new_mark
            print(f"Updated marks for {update_name}: {students[update_name]}")
        else:
            print("Invalid subject number. Please enter 1, 2, or 3.")
        cont = input("Do you want to update another subject for this student? (yes/no): ").strip().lower()
        if cont != "yes":
            break
else:
    print("Student not found.")