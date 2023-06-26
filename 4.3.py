numbers = [] 
number = int(input("Введите целое число 0-выход: ")) 
 
while number != 0: 
    numbers.append(number) 
    number = int(input("Введите целое число 0-выход: ")) 
 
if len(numbers) > 0: 
    maximum = max(numbers) 
    minimum = min(numbers) 
    average = sum(numbers) / len(numbers) 
 
    print("Максимальное значение:", maximum) 
    print("Минимальное значение:", minimum) 
    print("Среднее арифметическое:", average) 
else: 
    print("Вы не ввели ни одного числа.")