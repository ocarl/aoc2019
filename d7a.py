from intcode import IntCode


def calc_thrust(inlist, program):
    A = IntCode(program, in_vals=[inlist[0], 0])
    A.run()
    B = IntCode(program, in_vals=[inlist[1], A.output])
    B.run()
    C = IntCode(program, in_vals=[inlist[2], B.output])
    C.run()
    D = IntCode(program, in_vals=[inlist[3], C.output])
    D.run()
    E = IntCode(program, in_vals=[inlist[4], D.output])
    E.run()
    return E.output


assert str(calc_thrust([4, 3, 2, 1, 0], [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0])) == '43210'
assert str(calc_thrust([0,1,2,3,4], [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0])) == '54321'
assert str(calc_thrust([1,0,4,3,2], [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0])) == '65210'

def calc_max(program):
    max_thrust = 0
    max_settings = []
    for i in range(5):
        for j in range(5):
            for k in range(5):
                for l in range(5):
                    for m in range(5):
                        settings = [i,j,k,l,m]
                        if len(set(settings)) < 5:
                            continue
                        thrust = calc_thrust(settings, program)
                        if thrust > max_thrust:
                            max_thrust = thrust
                            max_settings = settings
    return max_thrust, max_settings

assert calc_max([3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]) == (43210, [4,3,2,1,0])
assert calc_max([3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]) == (54321, [0,1,2,3,4])
assert calc_max([3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]) == (65210, [1,0,4,3,2])

with open('input7.txt') as f:
    program = [int(x) for x in f.read().split(',')]
    max_thrust, _ = calc_max(program)
    print(max_thrust)


