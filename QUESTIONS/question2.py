#given two lists of integers write a program to merge them into a single list, 
# remove the lemetns that are common in both
list_1 = [1, 2, 3, 4, 5]
list_2 = [4, 5, 6, 7, 8]
list_3 = []
for i in list_1:
    if i not in list_2:
        list_3.append(i)
for i in list_2:
    if i not in list_1:
        list_3.append(i)
print("Merged List without common elements:", list_3)
