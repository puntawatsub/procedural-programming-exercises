import math
import random

name = input("name: ")
print("Hello,", name)

radius = float(input("radius of circle: "))
area = math.pi * (radius ** 2)
print("Area of circle: " + str("{:.2f}".format(area)))

length = float(input("length of rectangle: "))
width = float(input("width of rectangle: "))
perimeter = (length * 2) + (width * 2)
print("Perimeter of rectangle: " + str(perimeter))

num1 = int(input("first number: "))
num2 = int(input("second number: "))
num3 = int(input("third number: "))

sum = num1 + num2 + num3
average = sum / 3.0
print("The sum is:", sum)
print("The average is: " + str(average))
print("The product is:", num1 * num2 * num3);

talents = float(input(f"Enter talents: \n"))
pounds = float(input(f"Enter pounds: \n")) + (talents * 20)
lots = float(input(f"Enter lots: \n")) + (pounds * 32)

grams = lots * 13.3
kilograms = int((grams - (grams % 1000)) / 1000)
grams_left = grams - (kilograms * 1000)

print("The weight in modern units:")
print(str(kilograms), "kilograms and", str("{:.2f}".format(grams_left)), "grams.")

print(f"\n")

random_3_digits = ""
for i in range(3):
    random_3_digits += str(random.randint(0, 9))
print("3-digit code:", random_3_digits)

random_4_digits = ""
for i in range(4):
    random_4_digits += str(random.randint(1, 6))
print("4-digit code:", random_4_digits)