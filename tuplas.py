t1 = (1, 2, 3, 4, 'a')
t2 = (5, 6, 7)
t3 = t1 + t2

t1 = list(t1)
t1[1] = 3000
t1 = tuple(t1)

n1, n2, n3, *_, n7 = t3

for v in t1:
    print(v)