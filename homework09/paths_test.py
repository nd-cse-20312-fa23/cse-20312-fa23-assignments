#!/usr/bin/env python3

import itertools
import io
import doctest
import mypy.api
import unittest
import unittest.mock
import types

import paths
from tree import tree_read

# Paths Unit Tests

class PathsTests(unittest.TestCase):
    ''' Paths Unit Tests '''
    Total  = 3
    Points = 0
    Cases  = [
        ([1, 2, 3, 4]            , ([1, 2, 4], [1, 3])),
        ([9, 2, 8, 6, 0, 7]      , ([9, 2, 6], [9, 8, 7])),
        ([7, 1, 2, 4, 5, 8]      , ([7, 1, 4], [7, 1, 5], [7, 2, 8])),
        ([5, 3, 4, 6, 1, 0, 7, 8], ([5, 3, 6, 8], [5, 3, 1], [5, 4, 7])),
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
        failures, tests = doctest.testmod(paths, verbose=False)
        self.assertEqual(failures, 0)
        self.assertEqual(tests, 3)
        PathsTests.Points += 0.25

    def test_01_mypy(self):
        _, _, exit_status = mypy.api.run(['paths.py'])
        self.assertTrue(exit_status == 0)
        PathsTests.Points += 0.25

    def test_02_tree_paths(self):
        for array, results in self.Cases:
            root = tree_read(array)
            for expected, generated in itertools.zip_longest(results, paths.tree_paths(root)):
                self.assertEqual(expected, generated)
                PathsTests.Points += 0.125

    def test_03_main(self):
        case_input = io.StringIO('\n'.join(' '.join(map(str, a)) for a, _ in self.Cases))
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as output:
            paths.main(case_input)
            lines = output.getvalue().splitlines()

        case_output = []
        for _, results in self.Cases:
            case_output.extend([
                ', '.join(map(str, r)) for r in results
            ])
        for line, case_output in itertools.zip_longest(lines, case_output):
            self.assertEqual(line, case_output)
            PathsTests.Points += 0.125

# Main Execution

if __name__ == '__main__':
    unittest.main()
