lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []

for i in range(len(lst)):
    if i % 2 == 0:
        num = lst[i]
        if num == 2:
            result.append(num)
        elif num > 2:
            is_prime = True
            for j in range(2, num):
                if num % j == 0:
                    is_prime = False
                    break
            if is_prime:
                result.append(num)

print(result)  