import unittest
from project.vehicle import Vehicle


class VehicleTests(unittest.TestCase):

    DEFAULT_FUEL_CONSUMPTION = 1.25
    FUEL = 100
    CAPACITY = 101
    HORSE_POWER = 5

    def setUp(self):
        self.car = Vehicle(self.FUEL, self.HORSE_POWER)

    def test__init__(self):
        self.assertTrue(self.FUEL, self.car.fuel)
        self.assertTrue(self.FUEL, self.car.capacity)
        self.assertTrue(self.HORSE_POWER, self.car.horse_power)
        self.assertTrue(self.DEFAULT_FUEL_CONSUMPTION,
                        self.car.fuel_consumption)

    def test__drive__when_enough_fuel(self):
        kilometers = 10
        expected_fuel_needed = self.DEFAULT_FUEL_CONSUMPTION * kilometers

        self.car.drive(kilometers)

        expected = self.FUEL - expected_fuel_needed
        self.assertEqual(expected, self.car.fuel)

    def test__drive__when_max_possibel_distance(self):
        distance = self.FUEL / self.DEFAULT_FUEL_CONSUMPTION
        self.car.drive(distance)
        self.assertEqual(0, self.car.fuel)

    def test__drive__when_not_enough_fuel(self):

        with self.assertRaises(Exception) as ex:
            self.car.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test__refuel__if_needed(self):
        fuel_amount = 5
        self.car.fuel -= fuel_amount

        self.car.refuel(fuel_amount)
        self.assertEqual(self.FUEL, self.car.fuel)

    def test__refuel__when_not_needed(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(self.car.capacity + 1)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test__str__output(self):
        expected = f"The vehicle has {self.HORSE_POWER} horse power with {self.FUEL} fuel left and {self.DEFAULT_FUEL_CONSUMPTION} fuel consumption"
        self.assertEqual(expected, str(self.car))


if __name__ == '__main__':
    unittest.main()
