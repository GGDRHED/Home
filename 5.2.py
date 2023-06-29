codes = set()  
activat_code = input("Введите код активации: ")
if activat_code in codes: 
    print("Данный код уже был использован")
else:
    codes.add(activat_code)  
    print("Продукт активирован")