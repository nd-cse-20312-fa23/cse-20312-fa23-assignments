#!/usr/bin/env python3

import doctest
import unittest

import priority_queue

# Unit Tests

class PriorityQueueTest(unittest.TestCase):
    Data   = [9, 2, 8, 6, 7]
    Total  = 3
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
        self.assertEqual(tests, 15)

        PriorityQueueTest.Points += 0.75
    
    def test_01_constructor(self):
        p = priority_queue.PriorityQueue()
        self.assertEqual(p.data, [])
        
        p = priority_queue.PriorityQueue(self.Data)
        self.assertEqual(p.data, sorted(self.Data))
        
        PriorityQueueTest.Points += 0.5
    
    def test_02_push(self):
        p = priority_queue.PriorityQueue()
        self.assertEqual(p.data, [])
        
        for n in self.Data:
            p.push(n)
        
        self.assertEqual(p.data, sorted(self.Data))
        PriorityQueueTest.Points += 0.5
    
    def test_03_pop(self):
        p = priority_queue.PriorityQueue(self.Data)
        self.assertEqual(p.data, sorted(self.Data))
        
        for n in sorted(self.Data, reverse=True):
            self.assertEqual(p.pop(), n)

        PriorityQueueTest.Points += 0.5
    
    def test_04_front(self):
        p = priority_queue.PriorityQueue(self.Data)
        self.assertEqual(p.data, sorted(self.Data))
        
        for n in sorted(self.Data, reverse=True):
            self.assertEqual(p.front, n)
            self.assertEqual(p.pop(), n)

        PriorityQueueTest.Points += 0.25
    
    def test_05_empty(self):
        p = priority_queue.PriorityQueue()
        self.assertEqual(p.data, [])
        self.assertTrue(p.empty)
        
        for n in self.Data:
            p.push(n)
            self.assertFalse(p.empty)
        self.assertEqual(p.data, sorted(self.Data))
        
        for n in sorted(self.Data, reverse=True):
            self.assertEqual(p.front, n)
            self.assertEqual(p.pop(), n)
        self.assertTrue(p.empty)

        PriorityQueueTest.Points += 0.25

    def test_06_len(self):
        p = priority_queue.PriorityQueue()
        self.assertEqual(len(p), 0)
        
        p = priority_queue.PriorityQueue(self.Data)
        self.assertEqual(len(p), len(self.Data))

        PriorityQueueTest.Points += 0.25

# Main Execution

if __name__ == '__main__':
    unittest.main()

# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
