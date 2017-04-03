"""Unit tests
   Integration tests
   Acceptance test
   Create automated and repeatable tests

   TestCase - groups together related test functions
   fixtures - code run before and/or after each test function
   assertions - specific tests for conditions and behaviors
 """

import unittest

"""In test driven dev we write enough code to satisfy our test"""
def analyze_text():
    pass

class TextAnalysisTests(unittest.TestCase):
    """Tests for the `analyze_text()`."""

    def test_function_runs(self):
        """
            Start method name with test automaticaly
            detected by the library as test
            What it does:
                Does the function run at all?

        """
        analyze_text()

if __name__ == '__main__':
    unittest.main()
