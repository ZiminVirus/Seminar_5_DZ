# # 1) Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# print('Введите какой нибудь текст')
# text = input()
# print(text)
# text = text.split()
# result = list (filter(lambda word: 'а' not in word and 'б' not in word and 'в' not in word, text))
# print(result)

# 2) Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
with open('input.txt', 'r', encoding='utf-8') as file:
    word = list(file.read())
print(word)
word.append(0)

result = []
count = 1
i=0
for i in range (0, len(word) - 1):
    if word[i] == word[i+1]:
        count += 1
    else:
        result.append(count)
        result.append(word[i])
        count = 1
result = list(map (str, result))
print (result)
with open('output.txt', 'w', encoding='utf-8') as file:
    for i in range (0, len(result)):
        file.write(str(result[i]))

