import re
import string

#родительский класс с полем(переменная) self(this).string = string
class Str:
    def __init__(self,string):
        self.string = string
        
    def length(self):
        return len(self.string)

# Наследование от обычного класса строки. __init__ - конструктор, self = this.
class HexadecimalStr(Str):
    # (Строки данного класса могут содержать только
    # символы от '0' до 'f'. Если в инициализирующей строке есть хоть 1 другой символ =>
    # ШЕСТНАДЦАТИРИЧНАЯ СТРОКА = 0)
    def __init__(self, number):
        resultStr = ''
        strVal = str(number)
        if (self.isHexadecimal(strVal)):
            resultStr += strVal
        else:
            resultStr = '0'          
        print('Полученная строка:', resultStr)
        # При помощи super().__init__(resultStr) инициализируем поле string описанное в классе родителе получившейся строкой
        super().__init__(resultStr)
    
    def isHexadecimal (self, str):
        try:
            if int(str, 16):
                return True
            else:
                return False
        except ValueError:
            return False
    
    #перевод из 16-й систему в 10-ую
    def toDecimal (self):
        if (self.isHexadecimal(self.string)):
            newVal = int(self.string, 16)
            # self.string = str(newVal)
        # return self.string
        return newVal

    #перевод из 10-ой систему в 16-ую
    def toHexadecimal (self, strRes):
        newVal = int(strRes)
        newVal = hex(newVal)
        # self.string = str(newVal)
        # return self.string
        return newVal

    #проверка знака
    def checkMinusSign (self):
        if (self.string[0] == '-'):
            return True
        else:
            return False

    #интерпритация отрицательных чисел
    def changeSignToMinus (self):
        self.string = "-" + self.string

    #изменение знака на противоположный
    def changeSignToAnother (self):
        if (self.string[0] == "-"):
            self.string = self.string[1:]
        else:
            self.changeSignToMinus()
    
    def printAnswer (self, Result):
        print('Ответ в 10-й системе:', Result)
        print('Ответ в 16-ой системе:', self.toHexadecimal(str(Result)))
    
    #переопределение операций (длина строки результата >= длине большей из строк)
    def __ge__ (self, other):
        return self.toDecimal() >= other.toDecimal()

    #перегрузка арифметических операций

    # +
    def __add__(self, other):
        thisDecimal = self.toDecimal()
        otherDecimal = other.toDecimal()
        print('Первое число ИЗ 16-ой В 10-ую:', thisDecimal)
        print('Второе число ИЗ 16-ой В 10-ую:', otherDecimal)
        Result = int(otherDecimal) + int(thisDecimal) #str
        self.printAnswer(Result)

    # -
    def __sub__(self, other):
        thisDecimal = self.toDecimal()
        otherDecimal = other.toDecimal()
        print('Первое число ИЗ 16-ой В 10-ую:', thisDecimal)
        print('Второе число ИЗ 16-ой В 10-ую:', otherDecimal)
        Result = int(thisDecimal) - int(otherDecimal)
        self.printAnswer(Result)

    # *
    def __mul__(self, other):
        thisDecimal = self.toDecimal()
        otherDecimal = other.toDecimal()
        print('Первое число ИЗ 16-ой В 10-ую:', thisDecimal)
        print('Второе число ИЗ 16-ой В 10-ую:', otherDecimal)
        Result = int(thisDecimal) * int(otherDecimal)
        self.printAnswer(Result)

    # /
    def __truediv__(self, other):
        thisDecimal = self.toDecimal()
        otherDecimal = other.toDecimal()
        print('Первое число ИЗ 16-ой В 10-ую:', thisDecimal)
        print('Второе число ИЗ 16-ой В 10-ую:', otherDecimal)
        Result = int(thisDecimal) // int(otherDecimal)
        self.printAnswer(Result)

    # +=
    def __iadd__(self, other):
        thisDecimal = self.toDecimal()
        otherDecimal = other.toDecimal()
        print('Первое число ИЗ 16-ой В 10-ую:', thisDecimal)
        print('Второе число ИЗ 16-ой В 10-ую:', otherDecimal)
        firstDig = int(thisDecimal)
        secondDig = int(otherDecimal)
        firstDig = firstDig + secondDig
        self.printAnswer(firstDig)

    # -=
    def __isub__(self, other):
        thisDecimal = self.toDecimal()
        otherDecimal = other.toDecimal()
        print('Первое число ИЗ 16-ой В 10-ую:', thisDecimal)
        print('Второе число ИЗ 16-ой В 10-ую:', otherDecimal)
        firstDig = int(thisDecimal)
        secondDig = int(otherDecimal)
        firstDig = firstDig - secondDig
        self.printAnswer(firstDig)

    # *= 
    def __imul__(self, other):
        otherDecimal = other.toDecimal()
        thisDecimal = self.toDecimal()
        print('Первое число ИЗ 16-ой В 10-ую:', thisDecimal)
        print('Второе число ИЗ 16-ой В 10-ую:', otherDecimal)
        firstDig = int(otherDecimal)
        secondDig = int(thisDecimal)
        firstDig = firstDig * secondDig
        self.printAnswer(firstDig)

    # /=
    def __itruediv__(self, other):
        otherDecimal = other.toDecimal()
        thisDecimal = self.toDecimal()
        print('Первое число ИЗ 16-ой В 10-ую:', thisDecimal)
        print('Второе число ИЗ 16-ой В 10-ую:', otherDecimal)
        firstDig = int(otherDecimal)
        secondDig = int(thisDecimal)
        firstDig = firstDig // secondDig
        self.printAnswer(firstDig)


    


