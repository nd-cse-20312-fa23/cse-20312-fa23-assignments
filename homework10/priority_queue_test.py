#!/usr/bin/env python3

import doctest
import mypy.api
import unittest

import priority_queue

from priority_queue import PriorityQueue, left_index, right_index, parent_index
from heapq          import heapify, heappush, heappop

# Unit Tests

class PriorityQueueTests(unittest.TestCase):
    Data   = [9, 2, 8, 6, 7]
    Total  = 4
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
        failures, tests = doctest.testmod(priority_queue, verbose=False)
        self.assertEqual(failures, 0)
        self.assertEqual(tests, 19)
        PriorityQueueTests.Points += 0.25

    def test_01_mypy(self):
        _, _, exit_status = mypy.api.run(['priority_queue.py'])
        self.assertTrue(exit_status == 0)
        PriorityQueueTests.Points += 0.25

    def test_02_left_index(self):
        cases = [(0, 1), (1, 3), (2, 5), (4, 9)]
        for index, expected in cases:
            self.assertEqual(left_index(index), expected)
            PriorityQueueTests.Points += 0.05

    def test_03_right_index(self):
        cases = [(0, 2), (1, 4), (2, 6), (4, 10)]
        for index, expected in cases:
            self.assertEqual(right_index(index), expected)
            PriorityQueueTests.Points += 0.05

    def test_04_parent_index(self):
        cases = [(1, 0), (2, 0), (6, 2), (5, 2)]
        for index, expected in cases:
            self.assertEqual(parent_index(index), expected)
            PriorityQueueTests.Points += 0.025

    def test_05_bubble_up(self):
        cases = [
            ([2], [2]),
            ([2, 1], [1, 2]),
            ([2, 3, 1], [1, 3, 2]),
            ([2, 3, 4, 5, 6, 7, 8, 1], [1, 2, 4, 3, 6, 7, 8, 5])
        ]
        for original, expected in cases:
            pq = PriorityQueue(original)
            pq._bubble_up(len(original) - 1)
            self.assertEqual(pq.data, expected)
            PriorityQueueTests.Points += 0.125

    def test_06_push(self):
        bh = []
        pq = PriorityQueue()
        for value in self.Data:
            pq.push(value)
            heappush(bh, value)
            self.assertEqual(pq.data, bh)
            PriorityQueueTests.Points += 0.1

    def test_07_find_smallest_child(self):
        cases = [
            ([3, 2, 1], 0, 2),
            ([3, 1, 2], 0, 1),
            ([3, 1], 0, 1),
            ([2, 3, 4, 5, 6, 8, 7], 2, 6),
        ]
        for original, index, expected in cases:
            pq = PriorityQueue(original)
            self.assertEqual(pq._find_smallest_child(index), expected)
            PriorityQueueTests.Points += 0.125

    def test_08_bubble_down(self):
        cases = [
            ([2], [2]),
            ([3, 2], [2, 3]),
            ([3, 2, 1], [1, 2, 3]),
            ([9, 3, 4, 5, 6, 7, 8], [3, 5, 4, 9, 6, 7, 8]),
        ]
        for original, expected in cases:
            pq = PriorityQueue(original)
            pq._bubble_down(0)
            self.assertEqual(pq.data, expected)
            PriorityQueueTests.Points += 0.125

    def test_09_pop(self):
        bh = self.Data[:]
        heapify(bh)
        pq = PriorityQueue(bh[:])

        while pq.data:
            self.assertEqual(pq.pop(), heappop(bh))
            PriorityQueueTests.Points += 0.1

    def test_10_len(self):
        pq = PriorityQueue(self.Data[:])
        self.assertEqual(len(pq), len(self.Data))
        PriorityQueueTests.Points += 0.2

        pq.push(1)
        self.assertEqual(len(pq), len(self.Data) + 1)
        PriorityQueueTests.Points += 0.2

        pq.pop()
        self.assertEqual(len(pq), len(self.Data))
        PriorityQueueTests.Points += 0.1

# Main Execution

if __name__ == '__main__':
    unittest.main()

# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
