import random

def print_table(headers: list, data: list):
    col_width = 15

    # Print headers
    print("".join(header.ljust(col_width) for header in headers))

    # Print separator line
    print("-" * (col_width * len(headers)))

    # Print data rows
    for row in data:
        print("".join(str(item).ljust(col_width) for item in row))


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


class Elevator:
    def __init__(self, bottom_floor: int, top_floor: int):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.floor = bottom_floor
    
    def go_to_floor(self, floor_number: int):
        while self.floor < floor_number:
            self.floor_up()
        while self.floor > floor_number:
            self.floor_down()

    def floor_up(self):
        if not ((self.floor + 1) > self.top_floor):
            self.floor += 1
        print(f"Current floor: {self.floor}")

    def floor_down(self):
        if not ((self.floor - 1) < self.bottom_floor):
            self.floor -= 1
        print(f"Current floor: {self.floor}")


class Building:
    def __init__(self, bottom_floor: int, top_floor: int, elevators: int):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators: list[Elevator] = []
        for _ in range(elevators):
            self.elevators.append(Elevator(self.bottom_floor, self.top_floor))
        
    def run_elevator(self, elevator_number: int, destination: int):
        if elevator_number > len(self.elevators) or elevator_number < 1:
            print(f"Elevator out of range")
            return
        if destination < self.bottom_floor or destination > self.top_floor:
            print(f"Destination out of range")
        self.elevators[elevator_number - 1].go_to_floor(destination)
        print(f"Elevator No.{elevator_number} is at floor {self.elevators[elevator_number - 1].floor}")
    
    def fire_alarm(self):
        for i in range(len(self.elevators)):
            self.run_elevator(i + 1, self.bottom_floor)


elevator1 = Elevator(0, 12)

elevator1.go_to_floor(8)
elevator1.go_to_floor(elevator1.bottom_floor)

building1 = Building(-1, 12, 6)
building1.run_elevator(6, 12)
building1.fire_alarm()

class Race:
    def __init__(self, name: str, distance: float, cars: list[Car]):
        self.name = name
        self.distance = distance
        self.cars = cars
        self.hours = 0

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 16))
            car.drive(1)
        self.hours += 1
    
    def print_status(self):
        headers = ["Reg. No.", "Max Speed", "Distance", "Current Speed","Time"]
        info_list = []
        for car in self.cars:
            info_list.append([car.registration_number, car.maximum_speed, car.travelled_distance, car.current_speed, self.hours])
        print(f"Race: {self.name}")
        print_table(headers, info_list)
        print("\n")
    
    def race_finished(self) -> bool:
        is_race_finished = False
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                is_race_finished = True
                break
        return is_race_finished

car_list: list[Car] = []
for i in range(10):
    max_speed = random.randint(100, 201)
    registration_no = f"ABC-{i}"
    car_list.append(Car(registration_no, max_speed))

race1 = Race("Grand Demolition Derby", 8000, car_list)
while True:
    race1.hour_passes()
    if race1.race_finished():
        race1.print_status()
        break
    if race1.hours != 0 and race1.hours % 10 == 0:
        race1.print_status()

