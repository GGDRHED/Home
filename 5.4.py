text = input("Введите текст: ")

words = {}
for word in text.split():
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

max_count = 0
max_word = ""

for word, count in words.items():
    if count > max_count:
        max_count = count
        max_word = word

print("Самое часто встречающееся слово:", max_word)