# Write a program to input numbers and store them in a list. Then perform the following operations:
# i) Using built-in functions and without using built-in functions:
#    - Find max and min
#    - Sort them in ascending order
#    - Remove duplicate elements

numbers = []
n = int(input("Enter the number of terms: "))
for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

# Using built-in functions
max_num = max(numbers)
min_num = min(numbers)
sorted_numbers = sorted(numbers)
set = set(numbers)


print("Using built-in functions:")
print("Max:", max_num)
print("Min:", min_num)
print("Sorted List:", sorted_numbers)
print("Unique List:", set)

# Without using built-in functions
max_num = numbers[0]
min_num = numbers[0]
for i in range(1, n):
    if numbers[i] > max_num:
        max_num = numbers[i]
    if numbers[i] < min_num:
        min_num = numbers[i]


sorted_numbers_manual = numbers.copy()
for i in range(n):
    for j in range(n-i-1):
        if sorted_numbers_manual[i] < sorted_numbers_manual[j]:
            sorted_numbers_manual[i], sorted_numbers_manual[j] = sorted_numbers_manual[j], sorted_numbers_manual[i]
# Removing duplicates without built-in set
unique_numbers_manual = []
for item in numbers:
    if item not in unique_numbers_manual:
        unique_numbers_manual.append(item)

print("\nWithout using built-in functions:")
print("Max:", max_num)
print("Min:", min_num)
print("Sorted List:", sorted_numbers_manual)
print("Unique List:", unique_numbers_manual)



