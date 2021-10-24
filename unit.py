import unittest
from task3 import Justify_task
from task2 import Text_combination
from task1 import Reverse_numbers

class TestCalc(unittest.TestCase):
    def test_justify(self):
        exp_result = ['Hey  there mate,', 'it’s   nice   to', 'finally     meet', 'you!']
        task3 = Justify_task()
        self.assertEqual(task3.list_justify("Hey there mate, it’s nice to finally meet you!", 16), exp_result)

    def test_generete_letters(self):
        exp_result = ['gm', 'gn', 'go', 'hm', 'hn', 'ho', 'im', 'in', 'io']
        task2 = Text_combination()
        self.assertEqual(task2.generate_letters("46"), exp_result)

    def test_reverse_digits(self):
        exp_result = -3421
        task1 = Reverse_numbers()
        self.assertEqual(task1.reverse_digits(-1243), exp_result)

if __name__ == '__main__':
    unittest.main()
