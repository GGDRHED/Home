codes = set()
activat_code = input("Введите код активации: ")
if len(activat_code) != 10:
    print("Неправильный формат кода активации")
else:
    if activat_code in codes:
        print("Данный код уже был использован")
    else:
        codes.add(activat_code)
        print("Продукт активирован")
