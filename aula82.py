
x = 0
while x < 10:
    y = 0

    while y < 5:
        print(f'({x},{y})')
        y += 1

    x += 1 # x = x + 1

print('Acabou!')


x = 0
while x <= 100:
    if x == 3:
        x = x + 1
        continue

    print(x)
    x = x + 1

print('Acabou!')
