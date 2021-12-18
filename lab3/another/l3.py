# -*- coding: utf-8 -*-
""" Описать базовый класс СТРОКА. Описать производный от СТРОКА класс ВОСЬМЕРИЧНАЯ_СТРОКА. 
Строки данного класса могут содержать только символы от ‘0’ до ‘7’. Если в составе инициализирующей 
строки будут встречены любые символы, отличные от допустимых, ВОСЬМЕРИЧНАЯ_СТРОКА принимает нулевое значение. 
Содержимое данных строк рассматривается как восьмеричное число. Отрицательные числа хранятся в дополнительном коде.

Обязательные методы:

· изменение знака на противоположный (перевод числа в дополнительный код).

· Переопределить следующие операции (длина строки результата равна длине большей из строк; 
в случае необходимости более короткая битовая строка расширяется влево знаковым разрядом); 
1) возможность чтения из файла
2) возможность ввода вручную
3) переопределить +, -, *, /, +=, —= и все логические операции
4) Персональная задача указана у каждого, но помимо заданного метода необходимо определить методы, 
которые будут необходимы для проверки корректности работы, удобства работы 
и т.
5) сортировка массива из экземпляров класса (родителя и наследника) по одному из полей. 
Возможные алгоритмы: сортировка Шелла, быстрая сортировка, сортировка простыми вставками или шейкерная сортировка)
"""

from OctalStrings import OctalString

choice = int(input('Print 1 to read from file, any other key - read from keyboard\n'))

if (choice == 1):
    filename = input('enter filename\n')
    file = open(filename)
    nums = file.read().split()
    arr = []
    for num in nums:
        arr.append(OctalString(num))
    print('Octal view: ')
    for item in arr:
        print(item.toOctal(), end=' ')
    print()
    print('Decimal view: ')
    for item in arr:
        print(item.toDecimal(), end=' ')
    print()
    print()
    arr.sort()
    print('Sorted: ')
    for item in arr:
        print(item.toDecimal(), end=' ')
else:
    anum = int(input('enter a\n'))
    bnum = int(input('enter b\n'))
    a = OctalString(anum)
    b = OctalString(bnum)
    c = a + b
    print('decimal a: ' + str(a.toDecimal()))
    print('decimal b: ' + str(b.toDecimal()))

    print('plus result : ' + str(c.toOctal()) + ", decimal: " + str(c.toDecimal()))

    c = a - b
    print('minus result : ' + str(c.toOctal()) + ", decimal: " + str(c.toDecimal()))

    c = a * b
    print('multiply result : ' + str(c.toOctal()) + ", decimal: " + str(c.toDecimal()))

    c = a / b
    print('divide result : ' + str(c.toOctal()) + ", decimal: " + str(c.toDecimal()))

    a.changeSign()
    print('change a sign result : ' + str(c.toOctal()) + ", decimal: " + str(c.toDecimal()))


""" print('minus')
a = OctalString(744) # -28
b = OctalString(743) # -29
c = b - a # -29 + 28 = -1
d = a - b # -28 + 29 = -1

print(c.toDecimal())
print(d.toDecimal())
print()

print('plus')
a = OctalString(123) # 19
b = OctalString(164) # 52
c = a + b
print(c.toDecimal())
print()

print('mult')
a = OctalString(12)
b = OctalString(13)
c = a * b
print(c.toDecimal())
print()

print('div')
a = OctalString(15)
b = OctalString(13)
c = a / b
print(c.toDecimal())
print()

print('change sign')
a = OctalString(744) # -28
print(a.toDecimal())
a.changeSign()
print(a.toDecimal())
print()

arr = [OctalString(150), OctalString(75), OctalString(756), OctalString(7552), OctalString(744), OctalString(75), OctalString(15), OctalString(135)]

for string in arr:
    print(string.toDecimal(), end=' ')
print()
arr.sort()

for string in arr:
    print(string.toDecimal(), end=' ') """