#Write a program that receives a list of tuples representing (x, y) coordinates. Determine
#whether the points form a straight line.
points = []
n = int(input("Enter how many number of coordinates you want: "))
for i in range(n):
    x = int(input(f"Enter x for point{i+1}: "))
    y = int (input(f"Enter y for point {i+1}: "))
    points.append((x,y))

collinear = True 
if n > 2:
    x0, y0 = points[0]
    x1, y1 = points[1]
    for i in range(2,n):
        x,y = points [i]
        if (y1 - y0) * (x - x0) != (y - y0) * (x1 - x0):
            collinear = False
            break

if collinear:
    print("The points form a straight line.")
else:
    print("The points do NOT form a straight line.")