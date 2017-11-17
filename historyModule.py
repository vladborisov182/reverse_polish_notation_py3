#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv
import calc

class OperationsHistory():
    
    def add_history(self, expression, answer):
        row = [(expression, answer)]
        with open("history/history.csv", "a", newline = "") as file:
            writer = csv.writer(file, delimiter = '=')
            writer.writerows(row)


    def del_history(self):
        f = open("history/history.csv", "w")
        f.truncate()
        f.close()
        print ("История удалена")

    def read_history(self):
        with open("history/history.csv", "r") as file:
            reader = csv.reader(file)
            data_read = [row for row in reader]
            if not data_read:
                print ("История пуста")
            else:
                print ("История операций:")
                for expr in data_read:
                    print (expr)


if __name__ == '__main__':
    calc.main()