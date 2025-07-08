#wap to create a tuple of n numbers and then find 
# average of the numbers, median, mode 
import math
tuple = ()
n = int(input("Enter the number of elements you want to add to the tuple: "))
for i in range(n):
    element = int(input("Enter an element to add to the tuple: "))
    tuple += (element,)
print("Current Tuple:", tuple)
# Calculate average
average = sum(tuple) / n
print("Average:", average)
# Calculate median
sorted_tuple = sorted(tuple)
if n % 2 == 0:
    median = (sorted_tuple[n // 2 - 1] + sorted_tuple[n // 2]) / 2
else:
    median = sorted_tuple[n // 2]
print("Median:", median)
#calculate mode 
uniq = {}
for i in tuple:
    if i in uniq:
        uniq[i] += 1
    else:
        uniq[i] = 1
max_freq = max(uniq.values())
mode = [
    k for k, 
    v in uniq.items() 
        if v == max_freq
        ]

print("Mode:", mode) # here hamile loop ko through key check garyo then value check garyo ani respective value
# haru rakhyo .. matra max frequency ko value ra key ko pair print garxa 