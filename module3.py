print("Task 1: \n")
try:
    zanderLength = float(input("Zander length (cm): "))
except ValueError:
    raise ValueError("Value entered is not a number.")

if zanderLength < 42:
    print("The zander length does not meet the size threshold, please release the fish.")
    print("The fish was", str(42 - zanderLength) + "cm", "below the threshold.")
else:
    print("The zander is within the size threshold.")

print("")
print("Task 2: \n")

cabinClass = input("Cabin class: ")
if cabinClass == "LUX":
    print("upper-deck cabin with a balcony")
elif cabinClass == "A":
    print("above the car deck, equipped with a window")
elif cabinClass == "B":
    print("windowless cabin above the car deck")
elif cabinClass == "C":
    print("windowless cabin below the car deck")
else:
    raise ValueError("Cabin class entered is not valid.")

print("")
print("Task 3: \n")

while True:
    gender = input("Gender (M/F): ")
    if gender == "M" or gender == "F":
        break
    else:
        print("Please enter a valid gender.")
while True:
    try:
        hemoglobin = float(input("Hemoglobin (g/L): "))
        break
    except ValueError:
        pass
if gender == "F":
    if hemoglobin < 117:
        print("Your hemoglobin is too low.")
    elif hemoglobin > 155:
        print("Your hemoglobin is too high.")
    else:
        print("Your hemoglobin is normal.")
if gender == "M":
    if hemoglobin < 134:
        print("Your hemoglobin is too low.")
    elif hemoglobin > 167:
        print("Your hemoglobin is too high.")
    else:
        print("Your hemoglobin is normal.")

print("")
print("Task 4: Leap year calculation\n")

while True:
    try:
        year = int(input("Year: "))
        break
    except ValueError:
        pass
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
