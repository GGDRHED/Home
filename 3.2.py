t = 0 
p = float(input("Введите цену: ")) 
while p != 0: 
    t += p 
    p = float(input("Введите цену: ")) 
    d = t * 0.9 
print("Стоимость со скидкой:", d) 
print("Стоимость без скидки:", t)