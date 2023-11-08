import unittest
from math_quiz import random_number, random_operation, calculation


class TestMathGame(unittest.TestCase):

    def test_random_number(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for i in range(1000):  # Test a large number of random values
            rand_num = random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operation(self):
        for i in range(1000):  # Test a large number of random values
            RandOperation = random_operation()
            self.assertIn(RandOperation,"+-*","Operation does not exist!")
       

    def test_calculation(self):
        test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (5, 2, '*', '5 * 2', 10),
                (5, 2, '-', '5 - 2', 3),
                (33, 21, '-', '33 - 21', 12),
                (33, 21, '+', '33 + 21', 54),
                (33, 21, '*', '33 * 21', 693),
            ]

        for Num1, Num2, Operator, ExpectedProblem, ExpectedAnswer in test_cases:
            Problem, Answer = calculation(Num1, Num2, Operator)
            self.assertEqual(Answer,ExpectedAnswer, "The answer is not correct!")
            self.assertEqual(Problem, ExpectedProblem,"The problems are not the same!")
                

if __name__ == "__main__":
    unittest.main()
