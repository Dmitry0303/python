text1 = input('Введите 1-й текст ')
text2 = input('Введите 2-й текст ')
text3 = []
text1 = text1.lower()
text2 = text2.lower()
text1 = text1.split(' ')
text2 = text2.split(' ')
for i in text1:
    if i in text2 and i not in text3:
        text3.append(i)
print(f"Совпадения: {text3}")
