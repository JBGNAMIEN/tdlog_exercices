import unittest

from exo2 import Test


class TestSolution(unittest.TestCase):
    
    def test_fixed_true(self):
        fixed_tests_True = (
            ("samurai", "ai"),
            ("ninja", "ja"),
            ("sensei", "i"),
            ("abc", "abc"),
            ("abcabc", "bc"),
            ("fails", "ails"),
        )
        for string, ending in fixed_tests_True:
            with self.subTest(f"Testing {string} ends with {ending}"):
                self.assertTrue(Test.solution(string, ending))

    def test_fixed_false(self):
        fixed_tests_False = (
            ("sumo", "omo"),
            ("samurai", "ra"),
            ("abc", "abcd"),
            ("ails", "fails"),
            ("this", "fails"),
            ("spam", "eggs"),
        )
        for string, ending in fixed_tests_False:
            with self.subTest(f"Testing {string} does not end with {ending}"):
                self.assertFalse(Test.solution(string, ending))


if __name__ == '__main__':
    unittest.main()
