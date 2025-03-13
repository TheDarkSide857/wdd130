import math
side = float(input("What is the length of a side of the square? "))
area1 = side ** 2
print(f"The area of the square is: {area1}")
length = float(input("What is the length of the rectangle? "))
width = float(input("What is the width of the rectangle? "))
area2 = length * width
print(f"The area of the rectangle is: {area2}")
radius = float(input("What is the radius of the circle? "))
area3 = math.pi * radius ** 2
print(f"The area of the circle is: {area3}")