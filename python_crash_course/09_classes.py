#!/usr/bin/env python3

class Car():
    def __init__(self, brand, model, year=2021):
        self.brand = brand
        self.model = model
        self.year = year

    def vmax(self):
        print(f"vmax {self.brand.title()} {self.model.title()} is xxx km/h")

    def acceleration(self):
        print(f"acceleration {self.brand.title()} {self.model.title()} is xx s")

astra = Car('opel', 'astra')
astra.acceleration()
