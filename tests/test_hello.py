import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from assignment_01 import say_hello

"""
These are the tests for the assignment 01.
"""
class TestHello(unittest.TestCase):
    @weight(1)
    @number("1.1")
    def test_hello(self):
        """ Evaluate 'Hello' """
        response = say_hello("Hello")
        self.assertEqual(response,"Hello")

    @weight(1)
    @number("1.2")
    def test_greetings(self):
        """ Evaluate 'GReETinGs' """
        response = say_hello("GReETinGs")
        self.assertEqual(response,"Hello")

    @weight(1)
    @number("1.3")
    def test_hello_there(self):
        """ Evaluate 'Hello there' """
        response = say_hello("Hello there")
        self.assertEqual(response,"I'm sorry, I don't understand.")