import unittest
import sys
from io import StringIO
from atcoder_python_lessons.lesson_1 import lesson_1

class TestLesson1(unittest.TestCase):
    def test_case1(self):
        input_data = "1\n2 3\ntest\n"
        expected_output = "6 test\n"
        self.assert_output(input_data, expected_output)

    def test_case2(self):
        input_data = "7\n8 9\nhello\n"
        expected_output = "24 hello\n"
        self.assert_output(input_data, expected_output)

    def assert_output(self, input_data, expected_output):
        sys.stdin = StringIO(input_data)
        captured_output = StringIO()
        sys.stdout = captured_output
        # lesson_1.pyのmain関数を直接呼び出すのではなく、モジュールとして実行する
        # これにより、if __name__ == '__main__': のブロックが実行される
        import runpy
        runpy.run_path("/Users/shiro/dev/practice/AtCoder/study/atcoder_python_lessons/lesson_1/lesson_1.py", run_name="__main__")
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()

