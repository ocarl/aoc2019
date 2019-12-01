def calc_fuel(x):
    added_fuel = x//3 - 2
    if added_fuel <= 0:
        return 0
    else:
        return added_fuel + calc_fuel(added_fuel)

assert calc_fuel(14) == 2
assert calc_fuel(1969) == 966
assert calc_fuel(100756) == 50346

with open('input1.txt') as f:
    print(sum([calc_fuel(int(x)) for x in f.readlines()]))
