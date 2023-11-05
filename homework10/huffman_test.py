#!/usr/bin/env python3

import doctest
import io
import mypy.api
import unittest
import unittest.mock
import types

import huffman

# Huffman Unit Tests

class HuffmanTests(unittest.TestCase):
    ''' Huffman Unit Tests '''
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
        failures, tests = doctest.testmod(huffman, verbose=False)
        self.assertEqual(failures, 0)
        self.assertEqual(tests, 5)
        HuffmanTests.Points += 0.5

    def test_01_mypy(self):
        _, _, exit_status = mypy.api.run(['huffman.py'])
        self.assertTrue(exit_status == 0)
        HuffmanTests.Points += 0.5

    def test_02_count_frequencies(self):
        cases = [
            (
                'BACABA',
                {'B': 2, 'A': 3, 'C': 1}
            ),
            (
                'abbcccddddeeeeeffffff',
                {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
            ),
        ]

        for symbols, counts in cases:
            self.assertEqual(huffman.count_frequencies(symbols), counts)
            HuffmanTests.Points += 0.25

    def test_03_compute_compression_ratio(self):
        cases = [
            (
                'BACABA',
                {'B': '11', 'A': '0', 'C': '10'},
                '5.33',
            ),
            (
                'abbcccddddeeeeeffffff',
                {'a': '1110', 'b': '1111', 'c': '110', 'd': '00', 'e': '01', 'f': '10'},
                '3.29',
            ),
        ]

        for symbols, codes, expected in cases:
            ratio = huffman.compute_compression_ratio(symbols, codes)
            self.assertEqual(f'{ratio:.2f}', expected)
            HuffmanTests.Points += 0.25

    def test_04_main(self):
        cases = [
            (
                'BACABA',
                '''A 0
C 10
B 11
Ratio: 5.33
'''         ),
            (
                'abbcccddddeeeeeffffff',
                '''d 00
e 01
f 10
c 110
a 1110
b 1111
Ratio: 3.29
'''         ),
            (
                '''You left me
Just when I needed you
You set me back
Just when I thought I got back
''',
                '''e 011
  111
h 0000
\\n 0001
o 1001
u 1010
t 1101
c 00100
w 00101
Y 00110
m 00111
J 01000
k 01001
b 01010
a 01011
d 10000
n 10110
s 10111
I 11000
l 100010
f 100011
y 110010
g 110011
Ratio: 1.92
'''         ),
            (
                '''This is the last time
I made this mistake
Can't see the stars
Yeah, it's too late
To be with someone
Never find what you need
We gotta bail out
Yeah, I can't sleep
''',
                '''t 010
e 100
  110
h 0000
i 0110
s 1010
a 1011
l 00010
n 01111
o 11110
\\n 11111
r 000110
Y 000111
I 001000
T 001001
b 001010
w 001011
u 001100
, 001101
d 111001
' 111010
m 111011
k 0011100
C 0011101
f 0011110
y 0011111
v 0111000
p 0111001
W 0111010
g 0111011
c 1110000
N 1110001
Ratio: 1.87
'''         ),
        ]

        for input_string, expected_string in cases:
            with unittest.mock.patch('sys.stdout', new=io.StringIO()) as output:
                huffman.main(io.StringIO(input_string))
                self.assertEqual(output.getvalue(), expected_string)
                HuffmanTests.Points += 0.5

# Main Execution

if __name__ == '__main__':
    unittest.main()

# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
