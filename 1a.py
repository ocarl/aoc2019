def calc_fuel(x):
    return x//3 - 2

assert calc_fuel(12) == 2
assert calc_fuel(14) == 2
assert calc_fuel(1969) == 654
assert calc_fuel(100756) == 33583

with open('input1.txt') as f:
    print(sum([calc_fuel(int(x)) for x in f.readlines()]))
