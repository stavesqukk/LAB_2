#WRITE A PYTHON FUNCTION THAT ACCEPTS A LIST AND RETURNS A NEW LIST CONTAINING 
#ONLY THE ELEMENTS AT EVEN INDXES AND THOSE THAT ARE PRIME NUMBERS

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []

for i in range(len(lst)):
    # Check if index is even
    if i % 2 == 0:
        result.append(lst[i])
    # Check if index is prime (not the element)
    elif i > 1:
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            result.append(lst[i])

print(result)