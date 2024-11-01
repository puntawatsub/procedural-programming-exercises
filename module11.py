def task1():
    class Publication:
        def __init__(self, name: str):
            self.name = name

    class Book(Publication):
        def __init__(self, name: str, author: str, page_count: str):
            super().__init__(name)
            self.author = author
            self.page_count = page_count
        
        def print_information(self):
            info_str = f'"{self.name}" by {self.author}, {self.page_count} ' 
            print(info_str)

    class Magazine(Publication):
        def __init__(self, name: str, chief_editor: str):
            super().__init__(name)
            self.chief_editor = chief_editor
        
        def print_information(self):
            info_str = f'"{self.name}" by chief editor {self.chief_editor}'
            print(info_str)

    magazine1 = Magazine("Donald Duck", "Aki Hyyppä")
    book1 = Book("Compartment No. 6", "Rosa Liksom", 192)

    magazine1.print_information()
    book1.print_information()

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

        def drive(self, hours: float):
            self.travelled_distance += self.current_speed * hours

        def __str__(self):
            return f"Registration: {self.registration_number}\nMax Speed: {self.maximum_speed} km/h\nCurrent Speed: {self.current_speed} km/h\nTravelled Distance: {self.travelled_distance} km \n"
        
    class ElectricCar(Car):
        def __init__(self, registration_number: str, maximum_speed: float, kilowatt_hours: float, travelled_distance: float = 0):
            super().__init__(registration_number, maximum_speed, travelled_distance)
            self.kilowatt_hours = kilowatt_hours

    class GasolineCar(Car):
        def __init__(self, registration_number: str, maximum_speed: float, liters: float, travelled_distance: float = 0):
            super().__init__(registration_number, maximum_speed, travelled_distance)
            self.liters = liters
    
    electric1 = ElectricCar("ABC-15", 180, 52.5)
    gasoline1 = GasolineCar("ACD-123", 165, 32.3)

    electric1.accelerate(100)
    gasoline1.accelerate(120)

    electric1.drive(3)
    gasoline1.drive(3)

    print(f"Electric: {electric1.travelled_distance} km")
    print(f"Gasoline: {gasoline1.travelled_distance} km")

if __name__ == "__main__":
    task1
    task2()