#Write a program to input two sets of student roll numbers: one who play cricket and
#another who play football. Find:
#a. Students who play both sports
#b. Students who play only one sport
#c. Students who play neither (given a master list of all students)
cset = set()
fset = set()
master_set = set()

n = int(input("Enter the total number of students: "))

for i in range(n):
    roll = int(input(f"\nEnter roll number of student {i+1}: "))
    master_set.add(roll)
    
    print("What sport does this student play?")
    print("1. Cricket")
    print("2. Football")
    print("3. Both")
    print("4. None")
    choice = input("Enter choice (1/2/3/4): ")
    
    if choice == '1':
        cset.add(roll)
    elif choice == '2':
        fset.add(roll)
    elif choice == '3':
        cset.add(roll)
        fset.add(roll)

# Set operations
both_sports = cset & fset
only_one_sport = (cset - fset) | (fset - cset)
neither_sport = master_set - (cset | fset)

# Output
print("\n✅ Students who play both sports:", both_sports)
print("✅ Students who play only one sport:", only_one_sport)
print("✅ Students who play neither sport:", neither_sport)
