def task1():
    print("Task 1: Write a program that asks the user for a number of a month and then prints out the corresponding season (spring, summer, autumn, winter). Save the seasons as strings into a tuple in your program. We can define each season to last three months, December being the first month of winter.")
    seasons = ("winter", "spring", "summer", "autumn")
    month = int(input("Input the month number: "))
    if month in [12, 1, 2]:
        print("The season is", seasons[0])
    elif month in [3, 4, 5]:
        print("The season is", seasons[1])
    elif month in [6, 7, 8]:
        print("The season is", seasons[2])
    elif month in [9, 10, 11]:
        print("The season is", seasons[3])

def task2():
    print("Task 2: Write a program that asks the user to enter names until he/she enters an empty string. After each name is read the program either prints out New name or Existing name depending on whether the name was entered for the first time. Finally, the program lists out the input names one by one, one below another in any order. Use the set data structure to store the names.")
    names = set()
    while True:
        name_input = input("Input a name: ")
        if name_input == "":
            break
        if name_input in names:
            print("Existing name")
        else:
            print("New name")
            names.add(name_input)
    for name in names:
        print(name)

def task3():
    print("Task 3: Write a program for fetching and storing airport data. The program asks the user if they want to enter a new airport, fetch the information of an existing airport or quit. If the user chooses to enter a new airport, the program asks the user to enter the ICAO code and name of the airport. If the user chooses to fetch airport information instead, the program asks for the ICAO code of the airport and prints out the corresponding name. If the user chooses to quit, the program execution ends. The user can choose a new option as many times they want until they choose to quit. (The ICAO code is an identifier that is unique to each airport. For example, the ICAO code of Helsinki-Vantaa Airport is EFHK. You can easily find the ICAO codes of different airports online.")
    airports = dict()
    while True:
        print("New (N)/Fetch (F)/Quit (Q): ", end="")
        response = input()
        if response.upper() == "N":
            icao = input("Input the ICAO code: ").upper()
            airport_name = input("Input the name of the airport: ")
            if icao not in airports:
                airports[icao] = airport_name
            else:
                print("Airport exist")
        elif response.upper() == "F":
            icao = input("Input the ICAO code: ").upper()
            if icao not in airports:
                print("Airport does not exist")
            else:
                print(airports[icao])
        elif response.upper() == "Q":
            break
        else:
            print("Invalid input")




if __name__ == "__main__":
    task1()
    task2()
    task3()