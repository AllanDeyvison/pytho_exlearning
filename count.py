from itertools import count

contador = count(start=5, step=2)

for v in contador:
    print(round(v, 2))

    if v >= 10:
        break