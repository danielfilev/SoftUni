import unittest
from project.plantation import Plantation


class PlantationTests(unittest.TestCase):

    SIZE = 10

    def setUp(self):
        self.plant = Plantation(self.SIZE)

    def test__init__(self):
        self.assertEqual(self.SIZE, self.plant.size)
        self.assertEqual({}, self.plant.plants)
        self.assertEqual([], self.plant.workers)

    def test__size_setter__not_working(self):

        with self.assertRaises(ValueError) as ex:
            self.plant.size = -1
        self.assertEqual("Size must be positive number!", (str(ex.exception)))

    def test__hire_worker__not_working(self):

        self.plant.workers = ["worker1"]
        with self.assertRaises(ValueError) as ex:
            self.plant.hire_worker("worker1")
        self.assertEqual("Worker already hired!", (str(ex.exception)))

    def test__hire_worker__working(self):

        self.plant.hire_worker("worker1")
        self.assertEqual(["worker1"], self.plant.workers)

    def test__len__(self):

        self.plant.plants = {"worker1": ["x", "y"], "b": ["z"]}
        expected = sum([len(plant) for plant in self.plant.plants.values()])
        result = len(self.plant)
        self.assertEqual(expected, result)

    def test__planting__not_working_worker_not_present(self):
        worker = "worker1"
        with self.assertRaises(ValueError) as ex:
            self.plant.planting(worker, "a")
        self.assertEqual(
            f"Worker with name {worker} is not hired!", str(ex.exception))

    def test__planting__not_working_not_enough_plants(self):

        plantie = Plantation(1)
        plantie.plants = {"worker1": ["x", "y"], "b": ["z"]}
        plantie.workers = ["worker1"]

        with self.assertRaises(ValueError) as ex:
            plantie.planting("worker1", "g")
        self.assertEqual("The plantation is full!", str(ex.exception))

    def test__planting__working_when_worker_is_in_use(self):

        worker = "worker1"
        j = "j"
        self.plant.workers = [worker]
        self.plant.plants = {worker: ["x", "y"], "b": ["z"]}
        expected = {worker: ["x", "y", "j"], "b": ["z"]}
        result = self.plant.planting(worker, j)
        self.assertEqual(expected, self.plant.plants)
        self.assertEqual(f"{worker} planted {j}.", result)

    def test__planting__working_when_worker_has_no_previous_plants(self):

        worker = "worker1"
        x = "x"
        self.plant.workers = [worker]
        self.plant.plants = {"b": ["z"]}
        expected = {worker: ["x"], "b": ["z"]}
        result = self.plant.planting(worker, x)
        self.assertEqual(f"{worker} planted it's first {x}.", result)
        self.assertEqual(expected, self.plant.plants)

    def test__str__method(self):
        self.plant.workers = ["worker1", "worker2"]
        self.plant.plants = {"worker1": ["x", "y"]}
        expected = f"Plantation size: {self.SIZE}\n" + \
            "worker1, worker2\n" + \
            f'worker1 planted: x, y'

        self.assertEqual(expected, str(self.plant))

    def test__repr__method(self):

        self.plant.workers = ["worker1", "worker2"]
        expected = f"Size: {self.SIZE}\n" + \
            f"Workers: worker1, worker2"

        self.assertEqual(expected, repr(self.plant))


if __name__ == '__main__':
    unittest.main()
