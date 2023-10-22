def find_common_participants(s1, s2, r=','):
    s1_1 = set(s1.split(r))
    s2_2 = set(s2.split(r))
    return s1_1.intersection(s2_2)


s1 = "Andrey,Dima,Nikita,Vitaliy"
s2 = "Dima,Vlad,Vitaliy,Artem,Pavel"
x = find_common_participants(s1, s2)
print(x)
print(sorted(x))
