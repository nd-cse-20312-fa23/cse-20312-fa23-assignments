#!/usr/bin/env python3

import io
import doctest
import mypy.api
import unittest
import unittest.mock
import types

import balanced

# Balanced Unit Tests

class BalancedTests(unittest.TestCase):
    ''' Balanced Unit Tests '''
    Total  = 2
    Points = 0
    Cases  = [
        ([5, 3, 6]                     , (True , 2)),
        ([5, 3, 6, 4]                  , (True , 3)),
        ([5, 3, 0, 4]                  , (False, 3)),
        ([5, 3, 4, 0, 1]               , (True , 3)),
        ([5, 3, 4, 6, 1, 0, 7, 8]      , (True , 4)),
        ([5, 3, 4, 0, 1, 0, 0, 0, 0, 2], (False, 4)),
    ]

    @classmethod
    def setupClass(cls):
        cls.Points = 0

    @classmethod
    def tearDownClass(cls):
        print()
        print(f'   Score {cls.Points:.2f} / {cls.Total:.2f}')
        print(f'  Status {"Success" if cls.Points >= cls.Total else "Failure"}')

    def test_00_doctest(self):
        failures, tests = doctest.testmod(balanced, verbose=False)
        self.assertEqual(failures, 0)
        self.assertEqual(tests, 4)
        BalancedTests.Points += 0.25

    def test_01_mypy(self):
        _, _, exit_status = mypy.api.run(['balanced.py'])
        self.assertTrue(exit_status == 0)
        BalancedTests.Points += 0.25

    def test_02_is_balanced(self):
        for array, result in self.Cases:
            self.assertEqual(balanced.is_balanced(array), result)
            BalancedTests.Points += 0.125

    def test_03_main(self):
        case_input = io.StringIO('\n'.join(' '.join(map(str, a)) for a, _ in self.Cases))
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as output:
            balanced.main(case_input)
            lines = output.getvalue().splitlines()

        case_output = ['Balanced' if r[0] else 'Not Balanced' for _, r in self.Cases]
        for line, case_output in zip(lines, case_output):
            self.assertEqual(line, case_output)
            BalancedTests.Points += 0.125

# Main Execution

if __name__ == '__main__':
    unittest.main()
