#!/usr/bin/env python3

import doctest
import mypy.api
import unittest
import types

import node
from node import Node, walk

# Node Unit Tests

class NodeTests(unittest.TestCase):
    ''' Node Unit Tests '''
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
        failures, tests = doctest.testmod(node, verbose=False)
        self.assertEqual(failures, 0)
        self.assertEqual(tests, 4)
        NodeTests.Points += 0.25

    def test_01_mypy(self):
        _, _, exit_status = mypy.api.run(['node.py'])
        self.assertTrue(exit_status == 0)
        NodeTests.Points += 0.25

    def test_02_comparison(self):
        self.assertTrue(Node('a', 1) > Node('b', 0))
        NodeTests.Points += 0.25

        self.assertFalse(Node('a', 1) == Node('b', 0))
        self.assertFalse(Node('a', 1) < Node('b', 0))
        NodeTests.Points += 0.25

    def test_03_walk(self):
        cases = [
            (
                Node('', 2, Node('A', 1), Node('B', 1)),
                {'A': '0', 'B': '1'}
            ),
            (
                Node('', 6, Node('A', 3), Node('', 3, Node('C', 1), Node('B', 2))),
                {'A': '0', 'C': '10', 'B': '11'}
            ),
            (
                Node('', 21, Node('', 9, Node('d', 4), Node('e', 5)), Node('', 12, Node('f', 6), Node('', 6, Node('c', 3), Node('', 3, Node('a', 1), Node('b', 2))))),
                {'d': '00', 'e': '01', 'f': '10', 'c': '110', 'a': '1110', 'b': '1111'}
            ),
            (
                Node('', 100, Node('f', 45), Node('', 55, Node('', 25, Node('c', 12), Node('d', 13)), Node('', 30, Node('', 14, Node('a', 5), Node('b', 9)), Node('e', 16)))),
                {'f': '0', 'c': '100', 'd': '101', 'e': '111', 'a': '1100', 'b': '1101'}
            )
        ]
        for tree, codes in cases:
            self.assertEqual(walk(tree), codes)
            NodeTests.Points += 0.25

# Main Execution

if __name__ == '__main__':
    unittest.main()

# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
