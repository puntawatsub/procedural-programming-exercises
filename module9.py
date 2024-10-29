import random

def print_table(headers: list ,data: list):
    col_width = 15

    # Print headers
    print("".join(header.ljust(col_width) for header in headers))

    # Print separator line
    print("-" * (col_width * len(headers)))

    # Print data rows
    for row in data:
        print("".join(str(item).ljust(col_width) for item in row))

def task1():
    class Car:
        def __init__(self, registration_number: str, maximum_speed: float, travelled_distance: float = 0):
            self._registration_number = registration_number
            self._maximum_speed = maximum_speed
            self._current_speed = 0
            self._travelled_distance = travelled_distance

        @property
        def current_speed(self):
            return self._current_speed

        @current_speed.setter
        def current_speed(self, value):
            self._current_speed = value

        @property
        def travelled_distance(self):
            return self._travelled_distance

        @travelled_distance.setter
        def travelled_distance(self, value):
            self._travelled_distance = value

        @property
        def registration_number(self):
            return self._registration_number

        @registration_number.setter
        def registration_number(self, value):
            self._registration_number = value

        @property
        def maximum_speed(self):
            return self._maximum_speed

        @maximum_speed.setter
        def maximum_speed(self, value):
            self._maximum_speed = value

        def __str__(self):
            return f"Registration: {self.registration_number}\nMax Speed: {self.maximum_speed} km/h\nCurrent Speed: {self.current_speed} km/h\nTravelled Distance: {self.travelled_distance} km \n"

    car1 = Car("ABC-123", 142)

    print(car1)

def task2():
    class Car:
        def __init__(self, registration_number: str, maximum_speed: float, travelled_distance: float = 0):
            self._registration_number = registration_number
            self._maximum_speed = maximum_speed
            self._current_speed = 0
            self._travelled_distance = travelled_distance

        @property
        def current_speed(self):
            return self._current_speed

        @current_speed.setter
        def current_speed(self, value):
            self._current_speed = value

        @property
        def travelled_distance(self):
            return self._travelled_distance

        @travelled_distance.setter
        def travelled_distance(self, value):
            self._travelled_distance = value

        @property
        def registration_number(self):
            return self._registration_number

        @registration_number.setter
        def registration_number(self, value):
            self._registration_number = value

        @property
        def maximum_speed(self):
            return self._maximum_speed

        @maximum_speed.setter
        def maximum_speed(self, value):
            self._maximum_speed = value

        # methods
        def accelerate(self, change: float):
            if change + self.current_speed > self.maximum_speed:
                self.current_speed = self.maximum_speed
            elif change + self.current_speed < 0:
                self.current_speed = 0
            else:
                self.current_speed += change

        def __str__(self):
            return f"Registration: {self.registration_number}\nMax Speed: {self.maximum_speed} km/h\nCurrent Speed: {self.current_speed} km/h\nTravelled Distance: {self.travelled_distance} km \n"

    car1 = Car("ABC-123", 142)
    car1.accelerate(30)
    car1.accelerate(70)
    car1.accelerate(50)
    print(f"Current Speed: {car1.current_speed} km/h")
    car1.accelerate(-200)
    print(f"Current Speed: {car1.current_speed} km/h")

def task3():
    class Car:
        def __init__(self, registration_number: str, maximum_speed: float, travelled_distance: float = 0):
            self._registration_number = registration_number
            self._maximum_speed = maximum_speed
            self._current_speed = 0
            self._travelled_distance = travelled_distance

        @property
        def current_speed(self):
            return self._current_speed

        @current_speed.setter
        def current_speed(self, value):
            self._current_speed = value

        @property
        def travelled_distance(self):
            return self._travelled_distance

        @travelled_distance.setter
        def travelled_distance(self, value):
            self._travelled_distance = value

        @property
        def registration_number(self):
            return self._registration_number

        @registration_number.setter
        def registration_number(self, value):
            self._registration_number = value

        @property
        def maximum_speed(self):
            return self._maximum_speed

        @maximum_speed.setter
        def maximum_speed(self, value):
            self._maximum_speed = value

        # methods
        def accelerate(self, change: float):
            if change + self.current_speed > self.maximum_speed:
                self.current_speed = self.maximum_speed
            elif change + self.current_speed < 0:
                self.current_speed = 0
            else:
                self.current_speed += change

        def drive(self, hours: float):
            self.travelled_distance += self.current_speed * hours

        def __str__(self):
            return f"Registration: {self.registration_number}\nMax Speed: {self.maximum_speed} km/h\nCurrent Speed: {self.current_speed} km/h\nTravelled Distance: {self.travelled_distance} km \n"

    car1 = Car("ABC-123", 142, 2000)
    car1.accelerate(60)
    car1.drive(1.5)
    print(car1)

def task4():
    class Car:
        def __init__(self, registration_number: str, maximum_speed: float, travelled_distance: float = 0):
            self._registration_number = registration_number
            self._maximum_speed = maximum_speed
            self._current_speed = 0
            self._travelled_distance = travelled_distance

        @property
        def current_speed(self):
            return self._current_speed

        @current_speed.setter
        def current_speed(self, value):
            self._current_speed = value

        @property
        def travelled_distance(self):
            return self._travelled_distance

        @travelled_distance.setter
        def travelled_distance(self, value):
            self._travelled_distance = value

        @property
        def registration_number(self):
            return self._registration_number

        @registration_number.setter
        def registration_number(self, value):
            self._registration_number = value

        @property
        def maximum_speed(self):
            return self._maximum_speed

        @maximum_speed.setter
        def maximum_speed(self, value):
            self._maximum_speed = value

        # methods
        def accelerate(self, change: float):
            if change + self.current_speed > self.maximum_speed:
                self.current_speed = self.maximum_speed
            elif change + self.current_speed < 0:
                self.current_speed = 0
            else:
                self.current_speed += change

        def drive(self, hours: float):
            self.travelled_distance += self.current_speed * hours

        def __str__(self):
            return f"Registration: {self.registration_number}\nMax Speed: {self.maximum_speed} km/h\nCurrent Speed: {self.current_speed} km/h\nTravelled Distance: {self.travelled_distance} km \n"

    car_list = []

    for i in range(10):
        max_speed = random.randint(100, 201)
        registration_no = f"ABC-{i}"
        car_list.append(Car(registration_no, max_speed))

    # race starts
    hours = 0
    while True:
        hours += 1
        finished = False
        for car in car_list:
            car.accelerate(random.randint(-10, 16))
            car.drive(1)
            if car.travelled_distance >= 10000:
                finished = True
        if finished:
            break
    info_list = []
    for car in car_list:
        info_list.append([car.registration_number, car.maximum_speed, car.travelled_distance, car.current_speed, hours])
    headers = ["Reg. No.", "Max Speed", "Distance", "Current Speed","Time"]
    print_table(headers, info_list)

if __name__ == "__main__":
    task1()
    task2()
    task3()
    task4()