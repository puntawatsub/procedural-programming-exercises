import random
import math

def task1():
    print("Task 1: Write a function that returns a random dice roll between 1 and 6. The function should not have any parameters. Write a main program that rolls the dice until the result is 6. The main program should print out the result of each roll.")
    def dice_roll():
        return random.randint(1,6)
    while True:
        dice = dice_roll()
        print(dice)
        if dice == 6:
            break

def task2():
    print("Task 2: Modify the function above so that it gets the number of sides on the dice as a parameter. With the modified function you can for example roll a 21-sided role-playing dice. The difference to the last exercise is that the dice rolling in the main program continues until the program gets the maximum number on the dice, which is asked from the user at the beginning.")
    dice_side = int(input("Enter the number of sides on the dice: "))
    def dice_roll(side):
        return random.randint(1, side)
    while True:
        dice = dice_roll(dice_side)
        print(dice)
        if dice == dice_side:
            break

def task3():
    print("Task 3: Write a function that gets the quantity of gasoline in American gallons and returns the number converted to litres. Write a main program that asks for a volume in gallons from the user and converts the value to liters. The conversion must be done by using the function. Conversions continue until the user inputs a negative value.")
    def gallon_to_litre(gallon):
        return 3.78541 * gallon
    while True:
        gallon = float(input("Enter the volume of gasoline in gallons: "))
        if gallon < 0:
            break
        else:
            print("Litre value is:", gallon_to_litre(gallon))

def task4():
    print("Task 4: Write a function that gets a list of integers as a parameter. The function returns the sum of all the numbers in the list. For testing, write a main program where you create a list, call the function, and print out the value it returned.")
    def sum_list(l):
        total = 0
        for i in l:
            total += i
        return total
    list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # print(list_a)
    print(sum_list(list_a))

def task5():
    print("Task 5: Write a function that gets a list of integers as a parameter. The function returns a second list that is otherwise the same as the original list except that all uneven numbers have been removed. For testing, write a main program where you create a list, call the function, and then print out both the original as well as the cut-down list.")
    def remove_uneven(l):
        total = []
        for i in l:
            if i % 2 == 0:
                total.append(i)
        return total
    list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list_a)
    print(remove_uneven(list_a))

def task6():
    def pizza_size(diameter):
        return math.pi * ((diameter/2) ** 2)
    pizza1_diameter = float(input("Enter the diameter of pizza 1: "))
    pizza1_price = float(input("Enter the price of pizza 1: "))
    pizza2_diameter = float(input("Enter the diameter of pizza 2: "))
    pizza2_price = float(input("Enter the price of pizza 2: "))
    pizza1_value = pizza1_price / pizza_size(pizza1_diameter)
    pizza2_value = pizza2_price / pizza_size(pizza2_diameter)
    if pizza1_value > pizza2_value:
        print("Pizza 2 is cheaper than pizza 1")
    elif pizza1_value < pizza2_value:
        print("Pizza 1 is cheaper than pizza 2")
    else:
        print("Yeah, buy any. Literally the same.")

if __name__ == "__main__":
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()