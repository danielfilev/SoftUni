import unittest
from project.student import Student


class StudentTests(unittest.TestCase):

    NAME = "Issey"

    def setUp(self):
        self.student = Student(self.NAME)

    def test__init__without_courses(self):
        self.assertEqual(self.NAME, self.student.name)
        self.assertEqual(dict(), self.student.courses)

    def test__init__with_courses(self):
        course = {"Travis Scott Discography": [
            "Highest in the room", "Astroworld"]}
        student = Student(self.NAME, course)
        self.assertEqual(self.NAME, student.name)
        self.assertEqual(course, student.courses)

    def test__enroll__if_course_already_exists(self):
        course_name = "How to get sturdy 101"
        notes = ['nyc', 'bronx', 'harlem']
        mock_dict = {course_name: notes}

        student = Student(self.NAME, mock_dict)

        result = student.enroll(course_name, ["times_square"])
        expected_message = "Course already added. Notes have been updated."

        self.assertEqual(expected_message, result)
        self.assertEqual(
            ['nyc', 'bronx', 'harlem', 'times_square'], student.courses[course_name])

    def test__enroll__extends_course_when_notes_is_not_passed(self):
        course_name = "Dropshipping EZ"
        notes = ["Just don't be broke lol"]

        result = self.student.enroll(course_name, notes)
        expected_message = "Course and course notes have been added."

        self.assertEqual(expected_message, result)
        self.assertTrue(course_name in self.student.courses)
        self.assertEqual(notes, self.student.courses[course_name])

    def test__enroll__extends_course_when_notes_is_not_passed_Y(self):
        course_name = "Dropshipping EZ"
        notes = ["Just don't be broke lol"]

        result = self.student.enroll(course_name, notes, "Y")
        expected_message = "Course and course notes have been added."

        self.assertEqual(expected_message, result)
        self.assertTrue(course_name in self.student.courses)
        self.assertEqual(notes, self.student.courses[course_name])

    def test__enroll__if_course_doesn_not_exist(self):
        course_name = "How to sell drugs"
        notes = ["Don't get caught", "Don't get shanked"]

        result = self.student.enroll(course_name, notes, "No")
        expected_message = "Course has been added."

        self.assertEqual(expected_message, result)
        self.assertTrue(course_name in self.student.courses)
        self.assertEqual([], self.student.courses[course_name])

    def test__add_notes__if_course_already_added(self):
        course_name = "How to sell drugs"
        notes = ["Don't get caught", "Don't get shanked"]
        mock_course = {course_name: notes}

        student = Student(self.NAME, mock_course)
        added_notes = "Don't get shot"

        result = student.add_notes(course_name, added_notes)
        expected_message = "Notes have been updated"
        self.assertEqual(expected_message, result)
        self.assertEqual(
            ["Don't get caught", "Don't get shanked", "Don't get shot"], student.courses[course_name])

    def test__add_notes__if_course_not_added(self):
        course_name = "How to make money online"
        added_notes = "LMAOOO this mf reading this"

        with self.assertRaises(Exception) as ex:
            self.student.add_notes(course_name, added_notes)
        self.assertEqual(str(ex.exception),
                         "Cannot add notes. Course not found.")

    def test__leave__course_if_added(self):
        course_name = "How to make money online"
        notes = ["Don't get caught", "Don't get shanked"]

        self.student = Student(self.NAME, {course_name: notes})
        expected_message = "Course has been removed"
        result = self.student.leave_course(course_name)

        self.assertEqual(expected_message, result)
        self.assertTrue(course_name not in self.student.courses)

    def test__leave__course_if_not_added(self):
        course_name = "How to make money online"
        self.student.enroll("Python Cringe", [])

        with self.assertRaises(Exception) as ex:
            self.student.leave_course(course_name)
        self.assertEqual(str(ex.exception),
                         "Cannot remove course. Course not found.")


if __name__ == '__main__':
    unittest.main()
