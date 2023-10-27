#!/usr/bin/env python3

import doctest
import mypy.api
import unittest
import types

import tree
from tree import Node, tree_read, tree_values, tree_array

# Tree Unit Tests

class TreeTests(unittest.TestCase):
    ''' Tree Unit Tests '''
    Total  = 3
    Points = 0

    Tree1  = Node(value=1, left=Node(value=2, left=None, right=None), right=Node(value=3, left=None, right=None))
    Tree2  = Node(value=1, left=Node(value=2, left=Node(value=4, left=None, right=None), right=None), right=Node(value=3, left=None, right=Node(value=6, left=None, right=None)))

    @classmethod
    def setupClass(cls):
        cls.Points = 0

    @classmethod
    def tearDownClass(cls):
        print()
        print(f'   Score {cls.Points:.2f} / {cls.Total:.2f}')
        print(f'  Status {"Success" if cls.Points >= cls.Total else "Failure"}')

    def test_00_doctest(self):
        failures, tests = doctest.testmod(tree, verbose=False)
        self.assertEqual(failures, 0)
        self.assertEqual(tests, 3)
        TreeTests.Points += 0.5

    def test_01_mypy(self):
        _, _, exit_status = mypy.api.run(['tree.py'])
        self.assertTrue(exit_status == 0)
        TreeTests.Points += 0.5

    def test_02_tree_read(self):
        root = tree_read([1, 2, 3])
        self.assertTrue(isinstance(root, Node))
        self.assertEqual(root, self.Tree1)
        TreeTests.Points += 0.25

        root = tree_read([1, 2, 3, 4, 0, 0, 6])
        self.assertTrue(isinstance(root, Node))
        self.assertEqual(root, self.Tree2)
        TreeTests.Points += 0.25

    def test_03_tree_values(self):
        values = tree_values(self.Tree1)
        self.assertTrue(isinstance(values, types.GeneratorType))
        self.assertEqual(list(values), [2, 1, 3])
        TreeTests.Points += 0.25

        values = tree_values(self.Tree2)
        self.assertTrue(isinstance(values, types.GeneratorType))
        self.assertEqual(list(values), [4, 2, 1, 3, 6])
        TreeTests.Points += 0.25

    def test_04_tree_array(self):
        array = tree_array(self.Tree1)
        self.assertTrue(isinstance(array, list))
        self.assertEqual(array, [1, 2, 3])
        TreeTests.Points += 0.5

        array = tree_array(self.Tree2)
        self.assertTrue(isinstance(array, list))
        self.assertEqual(array, [1, 2, 3, 4, 0, 0, 6])
        TreeTests.Points += 0.5

# Main Execution

if __name__ == '__main__':
    unittest.main()
