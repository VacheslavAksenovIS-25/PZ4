import calculations as calc
import io

# Пример логики
num1 = io.get_number("Введите первое число: ")
num2 = io.get_number("Введите второе число: ")
result = calc.add(num1, num2)
io.display_result(result)