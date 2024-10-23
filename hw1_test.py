import math

import data
import hw1
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count_case1(self):
        # Test case 1: A simple string with a few vowels
        in_str = "Hello World"
        expected_output = 3  # 'e', 'o', 'o'
        assert hw1.vowel_count(in_str) == expected_output

    def test_vowel_count_case2(self):

        in_str = "bcdfg"
        expected_output = 0
        assert hw1.vowel_count(in_str) == expected_output

    # Part 2
    def test_short_lists_case1(self):
        input_list = [[1, 2], [3, 4, 5], [6, 7], [8]]
        expected_output = [[1, 2],[3,4,5] ,[6, 7]]
        self.assertEqual(hw1.short_lists(input_list), expected_output)

    def test_short_lists_case2(self):
        input_list = [[1], [3, 4, 5], [6, 7, 8], []]
        expected_output = [[3,4,5], [6,7,8]]
        self.assertEqual(hw1.short_lists(input_list), expected_output)


    # Part 3
    class TestCases(unittest.TestCase):

        def test_ascending_pairs_case1(self):
            input_list = [[4, 2], [3, 5, 1], [7, 7], [10]]
            expected_output = [[2, 4], [1, 3, 5], [7, 7], [10]]
            self.assertEqual(hw1.ascending_pairs(input_list), expected_output)

        def test_ascending_pairs_case2(self):
            input_list = [[1, 2], [5, 3, 4], [9, 8], []]
            expected_output = [[1, 2], [3, 4, 5], [8, 9], []]
            self.assertEqual(hw1.ascending_pairs(input_list), expected_output)


    # Part 4


    class TestCases(unittest.TestCase):

        def test_add_prices_case1(self):
            # Test case 1: No cents overflow
            price1 = hw1.Price(5, 50)
            price2 = hw1.Price(3, 25)
            result = hw1.add_prices(price1, price2)
            self.assertEqual(result.dollars, 8)
            self.assertEqual(result.cents, 75)

        def test_add_prices_case2(self):
            # Test case 2: Cents overflow
            price1 = hw1.Price(2, 60)
            price2 = hw1.Price(1, 50)
            result = hw1.add_prices(price1, price2)
            self.assertEqual(result.dollars, 4)
            self.assertEqual(result.cents, 10)



    # Part 5

        def test_rectangle_area_case1(self):
            rect = hw1.Rectangle(1, 5, 4, 1)
            expected_area = 12
            self.assertEqual(hw1.rectangle_area(rect), expected_area)

        def test_rectangle_area_case2(self):
            rect = hw1.Rectangle(2, 7, 5, 4)
            expected_area = 9
            self.assertEqual(hw1.rectangle_area(rect), expected_area)


    # Part 6


    class TestCases(unittest.TestCase):

        def test_books_by_author_case1(self):
            books = [
                hw1.Book("Book One", "Author A"),
                hw1.Book("Book Two", "Author B"),
                hw1.Book("Book Three", "Author A")
            ]
            author_name = "Author A"
            expected_books = [books[0], books[2]]  # Only books by "Author A"
            self.assertEqual(hw1.books_by_author(author_name, books), expected_books)

        def test_books_by_author_case2(self):
            books = [
                hw1.Book("Book One", "Author X"),
                hw1.Book("Book Two", "Author Y"),
                hw1.Book("Book Three", "Author Z")
            ]
            author_name = "Author A"
            expected_books = []
            self.assertEqual(hw1.books_by_author(author_name, books), expected_books)


    # Part 7
    import unittest
    import hw1  # Importing your hw1.py file

    class TestCases(unittest.TestCase):

        def test_circle_bound_case1(self):
            # Test case 1: A simple rectangle
            rect = hw1.Rectangle(0, 4, 4, 0)
            result = hw1.circle_bound(rect)
            expected_center_x = 2.0
            expected_center_y = 2.0
            expected_radius = math.sqrt(2 ** 2 + 2 ** 2)
            self.assertEqual(result.center_x, expected_center_x)
            self.assertEqual(result.center_y, expected_center_y)
            self.assertAlmostEqual(result.radius, expected_radius)

        def test_circle_bound_case2(self):
            rect = hw1.Rectangle(-3, 7, 5, -2)
            result = hw1.circle_bound(rect)
            expected_center_x = 1.0
            expected_center_y = 2.5
            expected_radius = math.sqrt((5 - 1) ** 2 + (-2 - 2.5) ** 2)
            self.assertEqual(result.center_x, expected_center_x)
            self.assertEqual(result.center_y, expected_center_y)
            self.assertAlmostEqual(result.radius, expected_radius)


    # Part 8


    def test_below_pay_average_case1(self):
        employees = [
            hw1.Employee("Alice", 50000),
            hw1.Employee("Bob", 60000),
            hw1.Employee("Charlie", 40000)
        ]
        expected_output = ["Charlie"]
        self.assertEqual(hw1.below_pay_average(employees), expected_output)

    def test_below_pay_average_case2(self):
        employees = [
            hw1.Employee("Alice", 50000),
            hw1.Employee("Bob", 50000),
            hw1.Employee("Charlie", 50000)
        ]
        expected_output = []
        self.assertEqual(hw1.below_pay_average(employees), expected_output)

    def test_below_pay_average_case3(self):
        employees = []
        expected_output = []
        self.assertEqual(hw1.below_pay_average(employees), expected_output)







if __name__ == '__main__':
    unittest.main()
