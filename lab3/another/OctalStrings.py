import re

class MyString:
    def __init__(self, string):
        self.string = string
    def length(self):
        return len(self.string)
    

class OctalString(MyString):
            
    def __init__(self, number):
        strValue = str(number)
        finalString = ''
        if (self.isValid(strValue)):
            finalString += strValue
        else:
            finalString = '0'
        
        super().__init__(finalString)
        
    def changeSign(self):
            decimalThis = self.toDecimal()
            tmp = OctalString(self.toOctal(-decimalThis))
            self.string = tmp.string

    def isValid(self, string):
        return re.match(r'([0-8])+$', string)
    
    def set(self, string):
        finalString = '0'
        if (self.isValid(str(string))):
            finalString = str(string)
        self.string = finalString

    def toDecimal(self):
        rank = self.length() - 2
        
        thisNum = self.string
        if (self.isNegative()):
            # считаем нули, из которых не можем вычесть 1
            current = self.length() - 1
            while (thisNum[current] == '0'):
                current -= 1
            
            # вычитание 1
            thisNum = thisNum[:current] + str(int(thisNum[current]) - 1) + thisNum[current + 1:]

            current += 1

            # ставим 7 там, где не смогли вычесть 1
            while (current < self.length()):
                thisNum = thisNum[:current] + '7' + thisNum[current + 1:]
                current += 1

            # меняем все числа, кроме первого: 7421 -> 7356
            i = 1
            while (i < self.length()):
                thisNum = thisNum[:i] + str(7 - int(thisNum[i])) + thisNum[i+1:]
                i += 1
            
            result = self.convertNegativeOctalToDecimal(rank, thisNum)
        else:
            result = self.convertPositiveOctalToDecimal(rank, thisNum)

        return result

    def convertNegativeOctalToDecimal(self, rank, string):
        result = 0
        while (rank != -1):
            result -= 8**rank * int(string[len(string) - rank - 1])
            rank -= 1
        return result

    def convertPositiveOctalToDecimal(self, rank, string):
        result = 0
        while (rank != -1):
            result += 8**rank * int(string[len(string) - rank - 1])
            rank -= 1
        return result

    def toOctal(self, number = None):
        if (number is None):
            number = self.toDecimal()

        if (number > 0):
            currentNumber = number
        if (number == 0):
            return '0'
        if (number < 0):
            currentNumber = -number

        result = ''

        while (currentNumber != 0):
            result = str(currentNumber % 8) + result
            currentNumber = int(currentNumber / 8)

        # Перевод в дополнительный код
        if (number < 0):
            i = 0
            while (i < len(result)):
                result = result[:i] + str(7 - int(result[i])) + result[i + 1:]
                i += 1
        
            # ищем место для +1
            current = len(result) - 1
            while (current >= 0 and result[current] == '7'):
                current -= 1
            
            if (current == -1): # нужен доп разряд
                result = '1' + result
                current = 1
            else:
                # прибавляем 1
                result = result[:current] + str(int(result[current]) + 1) + result[current + 1:]
                current += 1

            # Проставляем 0 там, где после +1 они должны появиться
            while (current < len(result)):
                result = result[:current] + '0' + result[current + 1:]
                current += 1

        if (number > 0):
            result = '0' + result
        else:
            result = '7' + result

        return result

    def getValue(self):
        return self.string

    def getReverseNumber(self, string):
        i = 1
        while (i < len(string)):
            string = string[:i] + str(7 - int(string[i])) + string[i+1:]
        return string

    def __add__(self, other):
        otherDecimal = other.toDecimal()
        thisDecimal = self.toDecimal()
        decimalResult = otherDecimal + thisDecimal
        octalResult = self.toOctal(decimalResult)
        return OctalString(str(octalResult))

    def __sub__(self, other):
        otherDecimal = other.toDecimal()
        thisDecimal = self.toDecimal()
        decimalResult = thisDecimal - otherDecimal
        octalResult = self.toOctal(decimalResult)
        return OctalString(str(octalResult))

    def __mul__(self, other):
        otherDecimal = other.toDecimal()
        thisDecimal = self.toDecimal()
        decimalResult = thisDecimal * otherDecimal
        octalResult = self.toOctal(decimalResult)
        return OctalString(str(octalResult))

    def __truediv__(self, other):
        otherDecimal = other.toDecimal()
        thisDecimal = self.toDecimal()
        decimalResult = thisDecimal // otherDecimal
        octalResult = self.toOctal(decimalResult)
        return OctalString(str(octalResult))

    def __iadd__(self, other):
        otherDecimal = other.toDecimal()
        thisDecimal = self.toDecimal()
        decimalResult = otherDecimal + thisDecimal
        octalResult = self.toOctal(decimalResult)
        return OctalString(str(octalResult))

    def __isub__(self, other):
        otherDecimal = other.toDecimal()
        thisDecimal = self.toDecimal()
        decimalResult = thisDecimal - otherDecimal
        octalResult = self.toOctal(decimalResult)
        return OctalString(str(octalResult))

    def __imul__(self, other):
        otherDecimal = other.toDecimal()
        thisDecimal = self.toDecimal()
        decimalResult = thisDecimal * otherDecimal
        octalResult = self.toOctal(decimalResult)
        return OctalString(str(octalResult))

    def __itruediv__(self, other):
        otherDecimal = other.toDecimal()
        thisDecimal = self.toDecimal()
        decimalResult = thisDecimal // otherDecimal
        octalResult = self.toOctal(decimalResult)
        return OctalString(str(octalResult))

    def __lt__(self, other): # self < other
        return self.toDecimal() < other.toDecimal()

    def __le__(self, other): # self <= other
        return self.toDecimal() <= other.toDecimal()

    def __eq__(self, other): # self == other
        return self.toDecimal() == other.toDecimal()
    
    def __ne__(self, other): # self != other    
        return self.toDecimal() != other.toDecimal()

    def __gt__(self, other): # self > other
        return self.toDecimal() > other.toDecimal()
        
    def __ge__(self, other): # self >= other
        return self.toDecimal() >= other.toDecimal()

    def isNegative(self):
        return self.string[0] == '7' and len(self.string) > 1
