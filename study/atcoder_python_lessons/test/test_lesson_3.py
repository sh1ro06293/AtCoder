import unittest
import sys
from io import StringIO

class TestLesson3(unittest.TestCase):
    def test_case1(self):
        input_data = "4\n"
        expected_output = "Even\n"
        self.assert_output(input_data, expected_output)

    def test_case2(self):
        input_data = "5\n"
        expected_output = "Odd\n"
        self.assert_output(input_data, expected_output)

    def assert_output(self, input_data, expected_output):
        sys.stdin = StringIO(input_data)
        captured_output = StringIO()
        sys.stdout = captured_output
        import runpy
        runpy.run_path("/Users/shiro/dev/practice/AtCoder/study/atcoder_python_lessons/lesson_3/lesson_3.py", run_name="__main__")
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()

