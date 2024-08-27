import random
import hashlib

print("Task 1: Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.")
i = 0
while i < 1000:
    i += 1
    if i % 3 == 0:
        print(i)


print("Task 2: Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.")
while True:
    inches = float(input("Enter inches: "))
    if inches < 0:
        break
    print("Centimeter:", 2.54 * inches)

print("Task 3: Write a program that asks the user to enter numbers until they enter an empty string to quit. Finally, the program prints out the smallest and largest number from the numbers it received.")
smallest = None
largest = None
while True:
    numString = input("Enter a number: ")
    try:
        num = int(numString)
    except ValueError:
        if numString == "":
            break
        else:
            raise ValueError(f"invalid literal for int() with base 10: {numString}")
    if smallest is None and largest is None:
        smallest = num
        largest = num
    else:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
if smallest is not None and largest is not None:
    print("Largest number:", largest)
    print("Smallest number:", smallest)
elif smallest is None or largest is None:
    print("Not enough numbers were given")

print("Task 4: Write a game where the computer draws a random integer between 1 and 10. The user tries to guess the number until they guess the right number. After each guess the program prints out a text: Too high, Too low or Correct. Notice that the computer must not change the number between guesses.")
randomNumber = random.randint(1, 10)
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == randomNumber:
        print("Correct")
        break
    elif guess < randomNumber:
        print("Too low")
    elif guess > randomNumber:
        print("Too high")

print("Task 5: Write a program that asks the user for a username and password. If either or both are incorrect, the program ask the user to enter the username and password again. This continues until the login information is correct or wrong credentials have been entered five times. If the information is correct, the program prints out Welcome. After five failed attempts the program prints out Access denied. The correct username is python and password rules.")
username = "Python"
# password = "rules" # actually you should never store password in plain text so for a flex (lol) I will use hashing
passhash = "6c621d1a05138a7888d37d9269a9da8e2e11e4aced2f6cfd24b05ab1b9e61bb0"
count = 0
while True:
    if count != 0:
        print(count, "wrong password attempt(s)")
    if count >= 5:
        print("Access Denied")
        break
    username_input = input("Enter a username: ")
    password_input = input("Enter a password: ")

    password_input_hash = hashlib.sha256(password_input.encode('utf-8')).hexdigest()
    if username_input == username and password_input_hash == passhash:
        print("Welcome")
        break
    else:
        print("Invalid username or password")
        count += 1

print("Task 6: Estimate the value of pi")

accuracy = int(input("How accurate (number of dots to generate): "))

inside_circle = 0

for i in range(accuracy):
    random_dot = [random.uniform(-1, 1), random.uniform(-1, 1)]
    is_inside_circle = ((random_dot[0]**2 + random_dot[1]**2) < 1)
    if is_inside_circle:
        inside_circle += 1

estimated_pi = (inside_circle * 4) / accuracy
print("Estimated pi:", estimated_pi)

