#!/usr/bin/env python3

import itertools
import io
import doctest
import mypy.api
import unittest
import unittest.mock
import types

import invert
from tree import Node, tree_read, tree_values, tree_array

# Invert Unit Tests

class InvertTests(unittest.TestCase):
    ''' Invert Unit Tests '''
    Total  = 2
    Points = 0
    Cases  = [
        ([1, 2, 3]            , [1, 3, 2]),
        ([1, 2, 3, 4, 0, 0, 6], [1, 3, 2, 6, 0, 0, 4]),
        ([9, 2, 8, 6, 0, 7]   , [9, 8, 2, 0, 7, 0, 6]),
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
        failures, tests = doctest.testmod(invert, verbose=False)
        self.assertEqual(failures, 0)
        self.assertEqual(tests, 3)
        InvertTests.Points += 0.25

    def test_01_mypy(self):
        _, _, exit_status = mypy.api.run(['invert.py'])
        self.assertTrue(exit_status == 0)
        InvertTests.Points += 0.25

    def test_02_tree_invert(self):
        for original, inverted in self.Cases:
            original = tree_read(original)
            inverted = tree_read(inverted)
            self.assertEqual(invert.tree_invert(original), inverted)
            InvertTests.Points += 0.25

    def test_03_main(self):
        case_input = io.StringIO('\n'.join(' '.join(map(str, o)) for o, _ in self.Cases))
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as output:
            invert.main(case_input)
            lines = output.getvalue().splitlines()

        case_output = []
        for o, i in self.Cases:
            case_output.append(', '.join(map(str, o)))
            case_output.append(', '.join(map(str, i)))

        for line, case_output in itertools.zip_longest(lines, case_output):
            self.assertEqual(line, case_output)
            InvertTests.Points += 0.125

# Main Execution

if __name__ == '__main__':
    unittest.main()
