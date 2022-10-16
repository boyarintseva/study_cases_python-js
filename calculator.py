"""Скрипт простого калькулятора (для 2 аргументов), с валидацией"""

import math

# ввод данных и валидация 1 аргумента
print ("Этот калькулятор умеет производить простые арифметические действия с двумя числами.")
print ("Введите первое число: ")
var_1 = input()
while not type(var_1) == float:
    try:
        var_11 = float(var_1)
        break
    except:
        print("Это не число. Попробуйте еще:")
        var_1 = input()

# ввод данных и валидация знака
print("Введите действие (+, -, * или /): ")
znak = input()
znak_valid = ["+", "-", "*", "/"]
while not znak in znak_valid:
    print("Некорректный знак операции. Попробуйте снова: ")
    znak = input()

# ввод данных и валидация 2 аргумента
print ("Введите второе число: ")
var_3 = input()
while not type(var_3) == float:
    if znak == "/" and var_3 == "0":
        print("Деление на ноль невозможно, введите другое число:")
        var_3 = input()
    else:
        try:
            var_33 = float(var_3)
            break
        except:
            print("Это не число. Попробуйте еще:")
            var_3 = input()

# анализ знака и выбор действия с аргументами

if znak == "+":
    s = math.fsum([var_11, var_33])
if znak == "-":
    s = var_11 - var_33
if znak == "/":
        s = var_11 / var_33
if znak == "*":
    s = var_11 * var_33

# вывод результата: если результат - целое число, то выводим без десятичной части
if int(s) == s:
    s_result = int(s)
else:
    s_result = s
print("Результат:" + " "  + str(s_result))