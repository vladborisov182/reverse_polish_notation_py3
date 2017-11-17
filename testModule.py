#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import calc
 
class convertInputToListTest(unittest.TestCase):
    
    def test_oneElement(self):
        self.assertEqual(calc.Calculator.convertInputToList(self, "2"), ["2"])

    def test_threeElements(self):
        self.assertEqual(calc.Calculator.convertInputToList(self, "2+2"), ["2", "+", "2"])
    
    def test_bigNumber(self):
        self.assertEqual(calc.Calculator.convertInputToList(self, "2007"), ["2007"])
    
    def test_twoBigNumbers(self):
        self.assertEqual(calc.Calculator.convertInputToList(self, "2007+30"), ["2007", "+", "30"])
    
    def test_fullEquation(self):
        self.assertEqual(calc.Calculator.convertInputToList(self, "2+2*2/(30-5)+2"), ["2", "+", "2", "*", "2", "/", "(", "30", "-", "5", ")", "+", "2"])


class calculationTest(unittest.TestCase):
    
    def test_oneElement(self):
        self.assertEqual(calc.Calculator.calculation(self, "2"), 2.0)

    def test_threeElements(self):
        self.assertEqual(calc.Calculator.calculation(self, ["2", "+", "2"]), 4.0)
    
    def test_bigNumber(self):
        self.assertEqual(calc.Calculator.calculation(self, ["2007"]), 2007.0)
    
    def test_twoBigNumbers(self):
        self.assertEqual(calc.Calculator.calculation(self, ["2007", "+", "30"]), 2037.0)
    
    def test_fullEquation(self):
        self.assertEqual(calc.Calculator.calculation(self, ["2", "+", "2", "*", "2", "/", "(", "30", "-", "5", ")", "+", "2"]), 4.16)
    
    def test_fewOperands(self):
        self.assertEqual(calc.Calculator.calculation(self, ["2", "+", "+"]), "Мало операндов")

    def test_manyOperands(self):
        self.assertEqual(calc.Calculator.calculation(self, ["2", "+", "2", "(", "2", ")"]), "Много операндов")
    
    def test_openParenthesis(self):
        self.assertEqual(calc.Calculator.calculation(self, ["2", "+", "2", "(", "(", "("]), 4.0)

    def test_closedParenthesis(self):
        self.assertEqual(calc.Calculator.calculation(self, ["2", "+", "2", ")", ")", ")"]), 4.0)

    def test_divisionByZero(self):
        self.assertEqual(calc.Calculator.calculation(self, ["2", "/", "0"]), "Деление на ноль")

    def test_operatorsPriority(self):
        self.assertEqual(calc.Calculator.calculation(self, ["2", "*", "1", "+", "1"]), 3.0)

if __name__ == '__main__':
    unittest.main()