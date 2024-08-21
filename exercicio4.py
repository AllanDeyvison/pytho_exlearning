
#n = input('Coloque um número:')
#n = int(n)

def fizz(num):
    if num % 5 == 0 and num % 3 == 0:
        return 'FizzBuzz'
    if num % 5 == 0:
        return 'Buzz'
    if  num % 3 == 0:
        return 'Fizz'
    return num



print(fizz(7))
print(fizz(10))
print(fizz(15))
print(fizz(22))








