text = input("Введите текст ")
symcnt = 0
for i in text:
    if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
        symcnt += 1
text = text.split(' ')
wordcnt = len(text)
print(f"Количество слов в тексте {wordcnt}")
print(f"Количество английских букв в тексте {symcnt}")
