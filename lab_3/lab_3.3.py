def count_letters(s):
    s = s.lower()
    if not s.isalpha():
        s2 = ""
        for i in s:
            if i.isalpha():
                s2 += i
        s = s2
    x = {}
    for i in s:
        x[i] = x.get(i, 0) + 1
    return x
def calculate_frequency(x):
    y = 0
    for i in x.values():
        y += i
    for key, value in x.items():
        x[key] = round(value/y,2)
    return x

x=("Вы работаете над проектом по анализу текстов, и вам нужно провести частотный анализ букв в заданном тексте."
   "Частотный анализ поможет вам определить, какие буквы встречаются чаще всего, и построить статистику их использования."
   "Задачу следует разбить на два этапа""")

col = count_letters(x)
col = calculate_frequency(col)
for key, value in col.items():
    print(f"{key}: {value}")