from functools import total_ordering
"""Класс RomanNumeral🌶️🌶️
Реализуйте класс RomanNumeral, описывающий число в римской системе счисления. При создании экземпляра класс должен принимать один аргумент:

number — число в римской системе счисления. Например, IV
Экземпляр класса RomanNumeral должен иметь следующее неформальное строковое представление:

<число в римской системе счисления>
Помимо этого, экземпляр класса RomanNumeral должен поддерживать приведение к типу int, при приведении к которому его значением должно являться целое число в десятичной системе счисления, которому он соответствует.

Также экземпляры класса RomanNumeral должны поддерживать между собой все операции сравнения с помощью операторов ==, !=, >, <, >=, <=.

Наконец, экземпляры класса RomanNumeral должны поддерживать между собой операции сложения и вычитания с помощью операторов + и - соответственно:

результатом сложения должен являться новый экземпляр класса RomanNumeral, представляющий сумму исходных
результатом вычитания должен являться новый экземпляр класса RomanNumeral, представляющий разность исходных
Примечание 1. Гарантируется, что из римского числа всегда вычитается строго меньшее римское число.

Примечание 2. Подробнее про римскую систему счисления можно почитать по ссылке.

Примечание 3. Не забывайте, что именно константу NotImplemented рекомендуется возвращать в методах, реализующих арифметические операции или операции сравнения, если эти операции для объектов каких-либо типов не определены.

Примечание 4. Никаких ограничений касательно реализации класса RomanNumeral нет, она может быть произвольной.

Примечание 5. Тестовые данные доступны по ссылкам:
"""

@total_ordering
class RomanNumeral:
    _roman = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500,
              'CM': 900, 'M': 1000}
    _d_roman = {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 20:
        'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC', 100: 'C', 200: 'CC', 300: 'CCC',
                400: 'CD',  500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 1_000: 'M',
                2000: 'MM', 3000: 'MMM'}


    def __init__(self, number):
        self.number = number
        self.ar = 0

    def __eq__(self, other):
        if isinstance(other, RomanNumeral):
            return self._to_int(self.number) == other._to_int(other.number)
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, RomanNumeral):
            return self._to_int(self.number) < other._to_int(other.number)
        else:
            return NotImplemented

    def __str__(self):
        return f'{self.number}'

    def _to_int(self, string):
        if len(string) == 1:
            lst = [self._roman[string[0]]]
        else:
            lst = [self._roman[c] for c in string]  # список с числами
            for c in range(0, len(lst) - 1):
                if c == 0:
                    if lst[c] < lst[c + 1]:
                        lst[c] *= -1
                else:
                    if lst[c - 1] <= lst[c] or lst[c] >= lst[c + 1]:
                        lst[c] *= 1
                    else:
                        lst[c] *= -1
        return int(sum(lst))

    def _to_roman(self, dig):
        dig = str(dig)
        s = ''
        for index, c in enumerate(reversed(dig), 0):
            s = self._d_roman[int(c) * (10 ** index)] + s
        return s

    def __add__(self, other):
        if isinstance(other, RomanNumeral):
            val = self._to_int(self.number) + other._to_int(other.number)
            return RomanNumeral(self._to_roman(val))
        else:
            return NotImplemented


    def __sub__(self, other):
        if isinstance(other, RomanNumeral):
            val = self._to_int(self.number) - other._to_int(other.number)
            return RomanNumeral(self._to_roman(val))
        else:
            return NotImplemented



    def __int__(self):
        return int(self._to_int(self.number))











