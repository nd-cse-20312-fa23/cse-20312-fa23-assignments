#!/usr/bin/env python3

import doctest
import io
import unittest
import unittest.mock

import cups

# Unit Tests

class CupsTest(unittest.TestCase):
    Cases  = {
        (1 ,4, 2): 4,
        (5, 4, 4): 7,
        (5, 0, 0): 5,
    }
    Total  = 2
    Points = 0

    @classmethod
    def setupClass(cls):
        cls.Points = 0

    @classmethod
    def tearDownClass(cls):
        print()
        print(f'   Score {cls.Points:.2f} / {cls.Total:.2f}')
        print(f'  Status {"Success" if cls.Points >= cls.Total else "Failure"}')

    def test_00_doctest(self):
        failures, tests = doctest.testmod(cups, verbose=False)
        self.assertEqual(failures, 0)
        self.assertEqual(tests, 5)

        CupsTest.Points += 0.5
    
    def test_01_fill_cups(self):
        for case_input, case_output in self.Cases.items():
            self.assertEqual(cups.fill_cups(case_input), case_output)
            CupsTest.Points += 0.25
    
    def test_02_main(self):
        case_input = io.StringIO('\n'.join(' '.join(map(str, c)) for c in self.Cases))
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as output:
            cups.main(case_input)
            lines = output.getvalue().splitlines()

        case_output = [str(v) for v in self.Cases.values()]
        for line, case_output in zip(lines, case_output):
            self.assertEqual(line, case_output)
            CupsTest.Points += 0.25

# Main Execution

if __name__ == '__main__':
    unittest.main()

# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
