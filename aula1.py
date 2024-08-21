print('Hello world!')

for n in range(1, 101):
    fizzBuzz = ""
    if n % 3 == 0:
        fizzBuzz = fizzBuzz + "Fizz"
    if n % 5 == 0:
        fizzBuzz = fizzBuzz + "Buzz"
    if n % 5 != 0 and n % 3 != 0:
        fizzBuzz = fizzBuzz + str(n)
    print(fizzBuzz)