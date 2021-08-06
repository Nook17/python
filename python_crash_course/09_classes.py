#!/usr/bin/env python3

class Car:
    def __init__(self, brand, model, year=2021):
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer = 0

    def vmax(self):
        print(f"vmax {self.brand.title()} {self.model.title()} is xxx km/h")

    def acceleration(self):
        print(f"acceleration {self.brand.title()} {self.model.title()} is xx s")

    def read_odometer(self):
        print(f"This car has {self.odometer} km on it")
    
    def write_odometer(self, value):
        self.odometer = value

class Engine:
    def __init__(self, type='V8'):
        self.type = type

    def engine_describe(self):
        print(F"Type engine is: {self.type}")

class ElectricCar(Car):
    def __init__(self, brand, model, year=0):
        super().__init__(brand, model, year)
        self.battery_size = 17
        self.engine = Engine(type)

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery_size")


astra = Car('opel', 'astra')
astra.acceleration()
astra.read_odometer()
astra.odometer = 150
astra.read_odometer()
astra.write_odometer(280)
astra.read_odometer()

tesla = ElectricCar('tesla', 'model S', 2020)
tesla.vmax()
tesla.describe_battery()
tesla.engine.type = 'R4'
tesla.engine.engine_describe()
