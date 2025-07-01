import unittest
import sys
from io import StringIO

class TestLesson6(unittest.TestCase):
    def test_case1(self):
        input_data = "3\napple\nbanana\norange\n"
        expected_output = "apple\nbanana\norange\n"
        self.assert_output(input_data, expected_output)

    def test_case2(self):
        input_data = "2\nhello\nworld\n"
        expected_output = "hello\nworld\n"
        self.assert_output(input_data, expected_output)

    def assert_output(self, input_data, expected_output):
        sys.stdin = StringIO(input_data)
        captured_output = StringIO()
        sys.stdout = captured_output
        import runpy
        runpy.run_path("/Users/shiro/dev/practice/AtCoder/study/atcoder_python_lessons/lesson_6/lesson_6.py", run_name="__main__")
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()

