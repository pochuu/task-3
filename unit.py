import unittest
import task3
import task2

class TestCalc(unittest.TestCase):
    def test_justify(self):
        exp_result = ['Hey  there mate,', 'it’s   nice   to', 'finally     meet', 'you!']
        self.assertEqual(task3.list_justify("Hey there mate, it’s nice to finally meet you!", 16), exp_result)

    def test_generete_letters(self):
        exp_result = ['gm', 'gn', 'go', 'hm', 'hn', 'ho', 'im', 'in', 'io']
        self.assertEqual(task2.generate_letters("46"), exp_result)

if __name__ == '__main__':
    unittest.main()
