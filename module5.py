import math
import random

def task1():
    print("Task 1: Write a program that asks the user how many dice to roll. The program rolls all the dice once and prints out the sum of the numbers. Use a for loop.")
    while True:
        try:
            dice = int(input("How many dice?: "))
            break
        except ValueError:
            pass
    dice_list = []
    for _ in range(dice):
        dice_list.append(random.randint(1,7))
    total = 0
    for i in dice_list:
        total += i
    print(f"The sum of all the dice is {total}")

def task2():
    print("Task 2: Write a program that asks the user to enter numbers until they input an empty string to quit. At the end, the program prints out the five greatest numbers sorted in descending order. Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument.")
    numbers = []
    while True:
        input_number = input("Enter a number: ")
        if input_number == "":
            break
        numbers.append(int(input_number))
    numbers.sort(reverse=True)
    print(numbers[0:5])

def task3():
    print("Task 3: Write a program that asks the user for an integer and tells if the number is a prime number. Prime numbers are number that are only divisible by one or the number itself.")
    input_number = int(input("Enter an integer: "))
    if input_number == 2 or input_number % 2 == 0 or input_number < 0:
        if input_number != 0:
            print("Not a prime number")
        else:
            print("Neither")
    else:
        for i in range(3, input_number, 2):
            if input_number % i == 0 or input_number == 1 :
                print("Not a prime number")
                break
        else:
            print("prime number")

def task4():
    print("Task 4: Write a program that asks the user to enter the names of five cities one by on (use a for loop for reading the names) and stores them into a list structure. Finally, the program prints out the names of the cities one by one, one city per line, in the same order they were read as input. Use a for loop for asking the names and a for/in loop to iterate through the list.")
    city_names = []
    for _ in range(5):
        city_names.append(input("Enter a city name: "))
    for city in city_names:
        print(city)


if __name__ == "__main__":
    task1()
    task2()
    task3()
    task4()