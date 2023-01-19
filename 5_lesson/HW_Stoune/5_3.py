# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res


def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            # print(txt[i])
            res = res + txt[i] * int(number)
            number = ''
    return res


tex_t = input("Введите текст для кодировки: ")
f = open('text_words.txt', 'w')
f.write(tex_t)
f.close()

f = open('text_words.txt', 'r', encoding='utf-8')
s = f.read()

str_code = coding(s)

f = open('text_code_words.txt', 'w')
f.write(str_code)
f.close()


print(f"Текст после кодировки: {coding(s)}")
print(f"Текст после дешифровки: {decoding(coding(s))}")
