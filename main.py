from string import punctuation
text = input("Введите текст: ")
text = text.lower()
for i in range(len(punctuation)):
    text = text.replace(punctuation[i], ' ')
words = text.split()
print(words)
print("Количество разных слов:", len(set(words)))
word_frequency = {}
for i in range(len(words)):
    if words[i] in word_frequency:
        word_frequency[words[i]] += 1
    else:
        word_frequency[words[i]] = 1
print('Частота слов: ')
for word, count in word_frequency.items():
    print(f'{word}: {count}')
symb_frequency = {}
for i in range(len(text)):
    if text[i] in symb_frequency:
        symb_frequency[text[i]] += 1
    else:
        symb_frequency[text[i]] = 1
print('Частота символов: ')
for symb, count in symb_frequency.items():
    print(f'{symb}: {count}')