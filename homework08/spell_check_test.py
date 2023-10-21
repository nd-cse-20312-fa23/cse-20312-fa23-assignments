#!/usr/bin/env python3

import doctest
import io
import unittest
import unittest.mock

import spell_check

# Unit Tests

class SpellCheckTest(unittest.TestCase):
    Cases = {
        'the'       : True,
        'thurr'     : False,
        'zoologist' : True,
        'Daedalae'  : False,
    }
    Poem  = ('''
’Twas brillig, and the slithy toves
Did gyre and gimble in the wabe:
All mimsy were the borogoves,
And the mome raths outgrabe.
''')
    Total  = 5
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
        failures, tests = doctest.testmod(spell_check, verbose=False)
        self.assertEqual(failures, 0)
        self.assertEqual(tests, 16)

        SpellCheckTest.Points += 1.0

    def test_01_word_list(self):
        words = spell_check.WordsList()
        self.assertTrue(isinstance(words.data, list))
        for case_input, case_output in self.Cases.items():
            self.assertEqual(case_input in words, case_output)
            SpellCheckTest.Points += 0.25

    def test_02_word_set(self):
        words = spell_check.WordsSet()
        self.assertTrue(isinstance(words.data, set))
        for case_input, case_output in self.Cases.items():
            self.assertEqual(case_input in words, case_output)
            SpellCheckTest.Points += 0.25

    def test_03_word_dict(self):
        words = spell_check.WordsDict()
        self.assertTrue(isinstance(words.data, dict))
        for case_input, case_output in self.Cases.items():
            self.assertEqual(case_input in words, case_output)
            SpellCheckTest.Points += 0.25

    def test_04_main_default(self):
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as output:
            spell_check.main('', io.StringIO(self.Poem))
            lines = output.getvalue().splitlines()

        self.assertTrue(len(lines) >= 9)
        self.assertEqual(lines[ 0], '’Twas')
        self.assertEqual(lines[-1], 'outgrabe.')
        SpellCheckTest.Points += 0.25

    def test_05_main_list(self):
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as output:
            spell_check.main('-l', io.StringIO(self.Poem))
            lines = output.getvalue().splitlines()

        self.assertTrue(len(lines) >= 9)
        self.assertEqual(lines[ 0], '’Twas')
        self.assertEqual(lines[-1], 'outgrabe.')
        SpellCheckTest.Points += 0.25

    def test_06_main_set(self):
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as output:
            spell_check.main('-s', io.StringIO(self.Poem))
            lines = output.getvalue().splitlines()

        self.assertTrue(len(lines) >= 9)
        self.assertEqual(lines[ 0], '’Twas')
        self.assertEqual(lines[-1], 'outgrabe.')
        SpellCheckTest.Points += 0.25

    def test_07_main_dict(self):
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as output:
            spell_check.main('-d', io.StringIO(self.Poem))
            lines = output.getvalue().splitlines()

        self.assertTrue(len(lines) >= 9)
        self.assertEqual(lines[ 0], '’Twas')
        self.assertEqual(lines[-1], 'outgrabe.')
        SpellCheckTest.Points += 0.25

# Main Execution

if __name__ == '__main__':
    unittest.main()

# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
