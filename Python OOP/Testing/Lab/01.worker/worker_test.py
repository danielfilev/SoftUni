import unittest
from worker_exercise.worker import Worker


class WorkerTests(unittest.TestCase):

    NAME = "Test Worker"
    SALARY = 1024
    ENERGY = 2

    def setUp(self):
        self.worker = Worker(self.NAME, self.SALARY, self.ENERGY)

    def testing__init__valid_props__expect_correct(self):
        self.assertEqual(self.NAME, self.worker.name)
        self.assertEqual(self.SALARY, self.worker.salary)
        self.assertEqual(self.ENERGY, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test__rest__incremented_energy(self):
        self.worker.rest()
        self.assertEqual(self.ENERGY + 1, self.worker.energy)

    def test__work__when_no_energy__expect_raise(self):
        worker = Worker(self.NAME, self.SALARY, 0)

        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertIsNotNone(ex)

    def test__work__when_enough_energy__expect_salary_to_be_increased(self):
        self.worker.work()
        self.worker.work()

        self.assertEqual(2 * self.SALARY, self.worker.money)

    def test__work__when_enough_energy__expect_energy_to_decrement(self):
        self.worker.work()

        self.assertEqual(self.ENERGY - 1, self.worker.energy)

    def test__get_info__expect_correct(self):

        actual_info = self.worker.get_info()
        expected_info = f'{self.NAME} has saved {self.worker.money} money.'

        self.assertEqual(expected_info, actual_info)


if __name__ == "__main__":
    unittest.main()
