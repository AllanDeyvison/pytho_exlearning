from itertools import combinations, permutations, product

people = ['Allan', 'Deyvison', 'Dias', 'Inocêncio']

for grup in product(people, repeat=2):
    print(grup)