#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import calc
 
class stringToListTest(unittest.TestCase):
    
    def test_oneElement(self):
        self.assertEqual(calc.Calculator.stringToList(self, "2"), ["2"])

    def test_threeElements(self):
        self.assertEqual(calc.Calculator.stringToList(self, "2 + 2"), ["2", "+", "2"])
    
    def test_bigNumber(self):
        self.assertEqual(calc.Calculator.stringToList(self, "2007"), ["2007"])
    
    def test_twoBigNumbers(self):
        self.assertEqual(calc.Calculator.stringToList(self, "2007+30"), ["2007", "+", "30"])
    
    def test_fullEquation(self):
        self.assertEqual(calc.Calculator.stringToList(self, "2+2*2/(30-5)+2"), ["2", "+", "2", "*", "2", "/", "(", "30", "-", "5", ")", "+", "2", ])


class infixToPostfixTest(unittest.TestCase):
    
    def test_oneElement(self):
        self.assertEqual(calc.Calculator.infixToPostfix(self, ["2"]), ["2"])

    def test_threeElements(self):
        self.assertEqual(calc.Calculator.infixToPostfix(self, ["2", "+", "2"]), ["2", "2", "+"])
    
    def test_bracketedEquation(self):
        self.assertEqual(calc.Calculator.infixToPostfix(self, ["(", "2", "+", "2", ")", "*", "10"]), ["2", "2", "+", "10", "*"])
    
    def test_extraParentheses(self):
        self.assertEqual(calc.Calculator.infixToPostfix(self, ["2", "+", "(", "(", "2", "*", "2", ")"]), ["2", "2", "2", "*", "+"])
    
    def test_permissibleError(self):
        self.assertEqual(calc.Calculator.infixToPostfix(self, ["2", "+", "2", "*", "2", "+", "("]), ["2", "2", "2", "*", "(", "+", "+"])


class reversedPolishNotationTest(unittest.TestCase):
    
    def test_oneElement(self):
        self.assertEqual(calc.Calculator.reversedPolishNotation(self, ["2"]), 2.0)
    
    def test_oneOperator(self):
        self.assertEqual(calc.Calculator.reversedPolishNotation(self, ["2", "+"]), "Мало операндов")

    def test_manyOperands(self):
        self.assertEqual(calc.Calculator.reversedPolishNotation(self, ["2", "2", "2", "+"]), "Много операндов")

    def test_fullEquation(self):
        self.assertEqual(calc.Calculator.reversedPolishNotation(self, ["2", "10", "+", "4", "5", "/", "3", "+", "-"]), 8.2)

    def test_permissibleError(self):
        self.assertEqual(calc.Calculator.reversedPolishNotation(self, ["2", "2", "2", "*", "(", "+", "+"]), "Мало операндов")

        

if __name__ == '__main__':
    unittest.main()