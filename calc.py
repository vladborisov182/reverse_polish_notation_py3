#!/usr/bin/python3
# -*- coding: utf-8 -*-

import historyModule


"""
Программа для вычисления выражений записанных в виде строки
reversedPolishNotation - главная функция вычисляющая выражение
"""

class Calculator():
    
    def convertInputToList(self, string):
    
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

    def calculation(self, expressionInfix):
        
        '''
        Включает в себя функции для преобразования выражения
        и его решения
        '''


        def convertInfixToPostfix(expressionInfix):
            
            '''
            Преобразовывает инфиксную запись
            выражения в постфиксную
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

            for i in range(0, len(expressionInfix)):
                try:
                    x = int(expressionInfix[i])
                    outputArray.append(expressionInfix[i])
                except:
                    if expressionInfix[i] is "(":
                        stack.append(expressionInfix[i])
                    elif expressionInfix[i] is ")":
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
                    elif expressionInfix[i] in operators:
                        try:
                            x = stack.pop()
                            stack.append(x)
                            if (operatorsPriority[expressionInfix[i]] == operatorsPriority[stack[-1]]):
                                outputArray.append(stack.pop())
                                stack.append(expressionInfix[i])
                            elif operatorsPriority[expressionInfix[i]] > operatorsPriority[stack[-1]]:
                                stack.append(expressionInfix[i])
                            elif operatorsPriority[expressionInfix[i]] < operatorsPriority[stack[-1]]:
                                outputArray.append(stack.pop())
                                stack.append(expressionInfix[i])
                            else:
                                outputArray.append(expressionInfix[i])
                        except:
                            stack.append(expressionInfix[i])
            while stack:
                outputArray.append(stack.pop())
            return outputArray
        
        def reversedPolishNotation(expr):
            
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
                        message = "Деление на ноль"
                        return message
                    stack.append(oper)

            if len(stack) != 1:
                message = "Много операндов"
                return message
            else:
                message = stack.pop()
                return message 
        
    
        #Вызов функции для преобразования инфиксной записи выражения в постфиксную
        polishNotation = convertInfixToPostfix(expressionInfix)


        # Вызов функции для решения выражения
        answer = reversedPolishNotation(polishNotation)

        #Возвращаем ответ или сообщение об ошибке
        return answer


def main():
        
    calc = Calculator()
    history = historyModule.OperationsHistory()

    print ("Доступные команды: \n w(work) - решить пример \n h(history) - посмотреть историю операций \n d(del) - очистить историю операций \n q(quit) - завершить программу")
    while True:
        s = input("Введите команду: ")
        if s == "q":
            print ("Программа завершена")
            break
        elif s == "h":
            history.read_history()
        elif s == "d":
            history.del_history()
        elif s == "w":
            
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


            expression = inputString
            

            #Вызов функции для преобразования строки в список
            expressionList = calc.convertInputToList(expression)

            #Вызов функции, которая возвращает результат вычисленного выражения 
            answer = calc.calculation(expressionList)

            history.add_history(expression, answer)

            #Вывод ответа или сообщения об ошибке
            print(" Ответ: %s \n" % (answer))
        
        else:
            print ("Неверная команда")
    
if __name__ == '__main__':
    main()





