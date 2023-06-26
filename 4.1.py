substring = input("Введите подстроку: ").lower()  
string = input("Введите строку: ").lower()  

if substring in string:
    print("Есть контакт!")
else:
    print("Мимо!")