"""
import unittest

def sum_numbers(numbers):
    numbers = [int(number) for number in numbers]
    return sum(numbers)

class TestCalk(unittest.TestCase):

    def test_isupper(self):
        numbers = [1,"2",3]
        self.assertEqual(sum_numbers(numbers), 6)


if __name__ == '__main__':
    unittest.main()
"""

# content of test_sample.py
def sum_numbers(numbers):
    numbers = [int(number) for number in numbers]
    return sum(numbers)

numbers = [1,"2",3]

def test_answer():
    assert sum_numbers(numbers) == 6