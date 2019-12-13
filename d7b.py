from intcode import IntCode


def calc_thrust(inlist, program):
    A = IntCode(program, in_vals=[inlist[0], 0])
    B = IntCode(program, in_vals=[inlist[1]])
    C = IntCode(program, in_vals=[inlist[2]])
    D = IntCode(program, in_vals=[inlist[3]])
    E = IntCode(program, in_vals=[inlist[4]])
    A.run()
    B.input = [inlist[1], A.output]
    B.run()
    C.input = [inlist[2], B.output]
    C.run()
    D.input = [inlist[3], C.output]
    D.run()
    E.input = [inlist[4], D.output]
    E.run()
    A.input = [inlist[0], E.output]
    while not E.stopped:
        A.run()
        B.input = [A.output]
        B.run()
        C.input = [B.output]
        C.run()
        D.input = [C.output]
        D.run()
        E.input = [D.output]
        E.run()
        A.input = [E.output]
    return E.output


def calc_max(program):
    max_thrust = 0
    max_settings = []
    for i in range(5,10):
        for j in range(5,10):
            for k in range(5,10):
                for l in range(5,10):
                    for m in range(5,10):
                        settings = [i,j,k,l,m]
                        if len(set(settings)) < 5:
                            continue
                        try:
                            thrust = calc_thrust(settings, program)
                        except IndexError:
                            continue
                        if thrust > max_thrust:
                            max_thrust = thrust
                            max_settings = settings
    return max_thrust, max_settings

assert calc_max([3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26, 27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]) == (139629729, [9,8,7,6,5])
assert calc_max([3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]) == (18216, [9,7,8,5,6])

with open('input7.txt') as f:
    program = [int(x) for x in f.read().split(',')]
    max_thrust, _ = calc_max(program)
    print(max_thrust)


