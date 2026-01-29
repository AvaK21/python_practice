"""Testing unit functions"""
import unittest

from mymodule import square, double

class TestSquare(unittest.TestCase):
    """
    Docstring for TestSquare
    """
    def test_1(self):
        """
        Docstring for test1
        
        :param self: Description
        """
        self.assertEqual(square(2),4) # test when 2 is given as input the putput is 4
        self.assertEqual(square(3.0),9.0) # test when 3.0 is given as input the output is 9.0
        self.assertEqual(square(-3), 9) # test when -3 is given as input the output is 9

class TestDouble(unittest.TestCase):
    """
    Docstring for TestDouble
    """
    def test_2(self):
        """
        Docstring for test2
        
        :param self: Description
        """
        self.assertEqual(double(2),4) # input 2, ouput is 4
        self.assertEqual(double(-3.1),-6.2) # input is -3.1, output is -6.2
        self.assertEqual(double(0),0) # test input 0, output is 0
#Line Below is important
#  for the tests to actually run when the file is executed - if on coursera lab
#unittest.main()
