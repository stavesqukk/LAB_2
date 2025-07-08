#11. Given a list of numbers with duplicates, use a set to remove the duplicates. Then,
#convert it back to a sorted list and display the result.
numbers = [1,2,3,4,2,5,4,6,7,899,33,434,11,11]
unique_set = set(numbers)
list2 = []
for i in unique_set:
    list2.append(i)
list2.sort()
print("The sorted list is: ")
print(list2)