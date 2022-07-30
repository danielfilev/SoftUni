from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):

    ac_consumption = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        fuel_needed = (self.fuel_consumption + self.ac_consumption) * distance

        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):

    ac_consumption = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        fuel_needed = (self.fuel_consumption + self.ac_consumption) * distance

        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += (fuel * 0.95)
        return self.fuel_quantity


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)    # 2.299999999999997
car.refuel(10)
print(car.fuel_quantity)    # 12.299999999999997
print()
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)  # 17.0
truck.refuel(50)
print(truck.fuel_quantity)  # 64.5
