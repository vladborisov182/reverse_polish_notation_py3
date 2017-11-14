#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Программа для вычисления выражений записанных в виде обратной
польской нотации.
reversedPolishNotation - главная функция вычисляющая выражение
"""

class Calculator():
    
    def stringToList(self, string):
    
        '''
        Записывает входную строку 
        в виде списка
        '''

        digits = "01234567890"
        list = []
        s = ""
        for i in range(0, (len(string))):
            if string[i] in "*/+-()":
                if s:
                    list.append(s)
                list.append(string[i])
                s = ""
            elif string[i] in digits:
                s = s + string[i]
                continue
        if string[(len(string)-1):] in digits:
            list.append(s)
        return list

    def infixToPostfix(self, equationList):
        
        '''
        Преобразовывает входные данные
        в обратную польскую запись
        '''

        # Приоритеты операторов:
        operatorsPriority = {
        "*" : 2,
        "/" : 2,
        "+" : 1,
        "-" : 1,
        }
        
        operators = ["+", "-", "/", "*"]

        stack = []
        outputArray = []

        for i in range(0, len(equationList)):
            try:
                x = int(equationList[i])
                outputArray.append(equationList[i])
            except:
                if equationList[i] is "(":
                    stack.append(equationList[i])
                elif equationList[i] is ")":
                    while True:
                        try:
                            oper = stack.pop()
                            if oper in operators:
                                outputArray.append(oper)
                            else:
                                try:
                                    oper =  stack.pop()
                                    if oper in operators:
                                        outputArray.append(oper)
                                except:
                                    break
                        except:
                            break
                elif equationList[i] in operators:
                    try:
                        x = stack.pop()
                        stack.append(x)
                        if (operatorsPriority[equationList[i]] == operatorsPriority[stack[-1]]):
                            outputArray.append(stack.pop())
                            stack.append(equationList[i])
                        elif operatorsPriority[equationList[i]] > operatorsPriority[stack[-1]]:
                            stack.append(equationList[i])
                        elif operatorsPriority[equationList[i]] < operatorsPriority[stack[-1]]:
                            outputArray.append(stack.pop())
                            stack.append(equationList[i])
                        elif x in "()":
                            stack.append(equationList[i])
                        else:
                            outputArray.append(equationList[i])
                    except:
                        stack.append(equationList[i])
        while stack:
            outputArray.append(stack.pop())
        return outputArray
    
    def reversedPolishNotation(self, expr):
        
        """
        Возвращает результат вычисленного выражения записанного в виде обратной
        польской нотации
        expr = list
        """

        operators = {
        '+': float.__add__, 
        '-': float.__sub__,
        '*': float.__mul__,
        '/': float.__truediv__,
    }   
        stack = [] 

        for element in expr:
            try:
                element = float(element)
                stack.append(element)
            except ValueError:
                if element not in operators: 
                    continue
                try:
                    oper2 = stack.pop()
                    oper1 = stack.pop()
                except IndexError:
                    message = "Мало операндов"
                    return message
                try:
                    oper = operators[element](oper1, oper2)
                except ZeroDivisionError:
                    message = "Нельзя делить на 0"
                    return message
                stack.append(oper)

        if len(stack) != 1:
            message = "Много операндов"
            return message
        else:
            message = stack.pop()
            return message  
    

# НАЧАЛО ПРОГРАММЫ

print ("Доступные команды: \n w(work) - решить пример \n s(story) - посмотреть историю операций \n d(del) - очистить историю операций \n q(quit) - завершить программу")
while True:
    s = input("Введите команду: ")
    if s is "q":
        print ("Программа завершена")
        break
    elif s is "s":
        print ("Функция 'история' еще не добавлена")
    elif s is "d":
        print ("Функция недоступна")
    elif s is "w":
        
        operators = ("1234567890+-/*()")
        print("Доступные операторы: +, -, *, /")

        '''
        Проверяет правильность ввода
        входного выражения
        '''

        while True:
            controlPoint = True
            inputString = str(input("Введите Ваш пример: "))
            for element in inputString:
                if element in operators:
                    continue
                else:
                    controlPoint = False
                    print("Недопустимые символы")
                    break
            if controlPoint is False:
                continue
            elif not inputString:
                print("Вы ничего не ввели")
                continue
            else:
                break


        equation = inputString
        calc = Calculator()

        #Вызов функции для преобразования строки в список
        equationList = calc.stringToList(equation)

        #Вызов функции, которая переводит пример в постфиксную запись
        polishNotation = calc.infixToPostfix(equationList)

        #Вызов функции, которая решает пример
        answer = calc.reversedPolishNotation(polishNotation)

        #Вывод ответа
        print(" Обратная польская запись: %s \n Ответ: %s \n" % (polishNotation, answer))
    else:
        print ("Неверная команда")
    






