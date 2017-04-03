"""Unit tests
   Integration tests
   Acceptance test
   Create automated and repeatable tests

   TestCase - groups together related test functions
   fixtures - code run before and/or after each test function
   assertions - specific tests for conditions and behaviors
 """
import os
import unittest

"""In test driven dev we write enough code to satisfy our test"""
def analyze_text(filename):
    """Return the number of lines and the number of characters in the file"""
    lines = 0
    chars = 0
    with open(filename, 'r') as f:
        for line in f:
            lines += 1
            chars += len(line)
    return (lines, chars)

class TextAnalysisTests(unittest.TestCase):
    """Tests for the `analyze_text()`."""

    def setUp(self):
        """Fixture that creates a file for the text methods to use"""
        self.filename = 'text_analysis_test_file.txt'
        with open(self.filename, 'w') as f:
            f.write('Now we are engaged in a great civil war.\n'
                    'testign whether that nation,\n'
                    'or any nation so conceived and dedicated,\n'
                    'can long endure')

    def tearDown(self):
        """Fixture that deletes the files used by the test methods"""
        try:
            os.remove(self.filename)
        except:
            pass

    def test_function_runs(self):
        """
            Start method name with test automaticaly
            detected by the library as test
            What it does:
                Does the function run at all?

        """
        analyze_text(self.filename)

    def test_line_count(self):
        """Check that the line count is correct."""
        self.assertEqual(analyze_text(self.filename)[0], 4)

    def test_character_count(self):
        """Check the character count is correct"""
        self.assertEqual(analyze_text(self.filename)[1], 127)

    def test_no_such_file(self):
        """Check the proper exception is thrown for a missing file."""
        with self.assertRaises(IOError):
            analyze_text('foobar')

    def test_no_deletion(self):
        """Check that the function doesn't delete the input file"""
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))

if __name__ == '__main__':
    unittest.main()
