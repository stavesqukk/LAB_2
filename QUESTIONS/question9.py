#9. Create a set of random numbers. Add more numbers until the set has 10 unique
#elements. Also, remove the smallest and largest element.
import random 
set1 = set()
while len(set1) < 10:
    set1.add(random.randint(1, 100)) 
print("Original set:", set1)
set1.remove(min(set1))
set1.remove(max(set1))

print("After removing smallest and largest:", set1)