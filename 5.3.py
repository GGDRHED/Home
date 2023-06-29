t = input("Введите текст: ")
w = t.split()
word_count = {}
for wo in w:
    if wo in word_count:
        word_count[wo] += 1
    else:
        word_count[wo] = 1
for wo, count in word_count.items():
    print(f"{wo}: {count}")