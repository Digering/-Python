def tovar(x, y):
    bool = False
    q = 0
    for i in x:
        if i == y:
            bool = not bool
            break
        q += 1
    if bool:
        return q
    else:
        return None

t = ['Яблоко', 'Ручка', 'Наклейка', 'Ручка', 'Ручка', 'Яблоко']
print(tovar(t, 'Наклейка'))
print(tovar(t, 'Фломастер'))
print(tovar(t, 'Яблоко'))