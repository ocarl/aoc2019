class Program:
    def __init__(self, l):
        self.program = l
        self.gen = enumerate(self.program)

    def __getitem__(self, key):
        if key > (len(self.program) - 1):
            for _ in range(key - len(self.program) + 1):
                self.program.append(0)
            next_i, _ = next(self.gen)
            self.reset(next_i)
        return self.program[key]

    def __setitem__(self, key, value):
        if key > (len(self.program) - 1):
            for _ in range(key - len(self.program)):
                self.program.append(0)
            self.program.append(value)
            next_i, _ = next(self.gen)
            self.reset(next_i)
        else:
            self.program[key] = value

    def reset(self, i=None):
        self.gen = enumerate(self.program)
        if i:
            for _ in range(i):
                next(self.gen)


class IntCode:
    def __init__(self, input_list, in_vals=[]):
        self.program = Program(input_list)
        self.output = None
        self.input = in_vals
        self.stopped = False
        self.relative_base = 0

    def run(self):
        self.input = iter(self.input)
        self.output = None
        while True:
            i, val = next(self.program.gen)
            op_code = val % 100
            param1_mode = int((val - op_code) % 1000 / 100)
            param2_mode = int((val - op_code - param1_mode) % 10000 / 1000)
            param3_mode = int(
                (val - op_code - param1_mode - param2_mode) % 100000 / 10000)
            if any(map(lambda x: x > 2, [param1_mode, param2_mode, param3_mode])):
                continue
            if op_code == 1:
                # add
                param_mode_list = [(self.program[i + 1], param1_mode),
                                   (self.program[i + 2], param2_mode),
                                   (self.program[i + 3], param3_mode)]
                self.operator(param_mode_list, fun=lambda x, y: x + y)
                for _ in range(len(param_mode_list)):
                    next(self.program.gen)
            elif op_code == 2:
                # multiply
                param_mode_list = [(self.program[i + 1], param1_mode),
                                   (self.program[i + 2], param2_mode),
                                   (self.program[i + 3], param3_mode)]
                self.operator(param_mode_list, fun=lambda x, y: x * y)
                for _ in range(len(param_mode_list)):
                    next(self.program.gen)
            elif op_code == 3:
                # read input
                param = self.program[i + 1]
                adress = self._write_adress((param, param1_mode))
                self.program[adress] = next(self.input)
                for _ in range(1):
                    next(self.program.gen)
            elif op_code == 4:
                # write output
                param = self._parse_operands([(self.program[i + 1], param1_mode)])[0]
                self.output = param
                for _ in range(1):
                    next(self.program.gen)
                break
            elif op_code == 5:
                # jump if true
                param_mode_list = [(self.program[i + 1], param1_mode),
                                   (self.program[i + 2], param2_mode),
                                   ]
                self.jump(param_mode_list, comp=lambda x: x != 0)
            elif op_code == 6:
                # jump if false
                param_mode_list = [(self.program[i + 1], param1_mode),
                                   (self.program[i + 2], param2_mode),
                                   ]
                self.jump(param_mode_list, comp=lambda x: x == 0)
            elif op_code == 7:
                # less than
                param_mode_list = [(self.program[i + 1], param1_mode),
                                   (self.program[i + 2], param2_mode),
                                   (self.program[i + 3], param3_mode)]
                self.store_bool(param_mode_list, comp=lambda x, y: x < y)
                for _ in range(len(param_mode_list)):
                    next(self.program.gen)
            elif op_code == 8:
                # equals
                param_mode_list = [(self.program[i + 1], param1_mode),
                                   (self.program[i + 2], param2_mode),
                                   (self.program[i + 3], param3_mode)]
                self.store_bool(param_mode_list, comp=lambda x, y: x == y)
                for _ in range(len(param_mode_list)):
                    next(self.program.gen)
            elif op_code == 9:
                # move relative base
                self.relative_base += self._parse_operands([(self.program[i + 1], param1_mode)])[0]
                next(self.program.gen)
            elif op_code == 99:
                self.stopped = True
                break
            else:
                continue

    def _parse_operands(self, param_mode_list):
        operands = []
        for param, mode in param_mode_list:
            if mode == 0:
                operands.append(self.program[param])
            if mode == 1:
                operands.append(param)
            if mode == 2:
                operands.append(self.program[self.relative_base + param])
        return operands

    def _write_adress(self, param_mode):
        adress = 0
        param, mode = param_mode
        if mode in [0, 1]:
            adress = param
        if mode == 2:
            adress = self.relative_base + param
        return adress

    def operator(self, param_mode_list, fun=lambda x, y: x + y):
        operands = self._parse_operands(param_mode_list[:-1])
        adress = self._write_adress(param_mode_list[-1])
        self.program[adress] = fun(*operands)

    def jump(self, param_mode_list, comp=lambda x: x != 0):
        operands = self._parse_operands(param_mode_list)
        if comp(operands[0]):
            self.program.reset(operands[1])

    def store_bool(self, param_mode_list, comp=lambda x, y: x < y):
        operands = self._parse_operands(param_mode_list[:-1])
        adress = self._write_adress(param_mode_list[-1])
        if comp(operands[0], operands[1]):
            self.program[adress] = 1
        else:
            self.program[adress] = 0


def test():
    # add test
    input_list = [1002, 4, 3, 4, 33]
    ic = IntCode(input_list)
    ic.run()
    assert ic.program[-1] == 99

    # compare tests
    input_list = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
    ic = IntCode(input_list, in_vals=[8])
    ic.run()
    assert ic.output == 1
    ic = IntCode(input_list, in_vals=[9])
    ic.run()
    assert ic.output == 0

    input_list = [3,9,7,9,10,9,4,9,99,-1,8]
    ic = IntCode(input_list, in_vals=[7])
    ic.run()
    assert ic.output == 1
    ic = IntCode(input_list, in_vals=[9])
    ic.run()
    assert ic.output == 0

    input_list = [3,3,1108,-1,8,3,4,3,99]
    ic = IntCode(input_list, in_vals=[8])
    ic.run()
    assert ic.output == 1
    ic = IntCode(input_list, in_vals=[9])
    ic.run()
    assert ic.output == 0

    input_list = [3,3,1107,-1,8,3,4,3,99]
    ic = IntCode(input_list, in_vals=[7])
    ic.run()
    assert ic.output == 1
    ic = IntCode(input_list, in_vals=[9])
    ic.run()
    assert ic.output == 0

    # jump tests
    input_list = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
    ic = IntCode(input_list, in_vals=[0])
    ic.run()
    assert ic.output == 0
    input_list = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
    ic = IntCode(input_list, in_vals=[1])
    ic.run()
    assert ic.output == 1

    input_list = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
    ic = IntCode(input_list, in_vals=[1])
    ic.run()
    #assert ic.output == 1
    #ic = IntCode(input_list, in_vals=[0])
    #ic.run()
    #assert ic.output == 0

    input_list = [
        3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006,
        20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46,
        104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99
    ]
    ic = IntCode(input_list, in_vals=[7])
    ic.run()
    assert ic.output == 999
    ic = IntCode(input_list, in_vals=[8])
    ic.run()
    assert ic.output == 1000
    ic = IntCode(input_list, in_vals=[9])
    ic.run()
    assert ic.output == 1001

    il = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    ic = IntCode(il.copy())
    out = []
    while len(out) != 16:
        ic.run()
        out.append(ic.output)
    assert il == out

    input_list = [
        1102, 34915192, 34915192, 7, 4, 7, 99, 0
    ]
    ic = IntCode(input_list.copy())
    ic.run()
    assert len(str(ic.output)) == 16

    input_list = [
        104,1125899906842624,99
    ]
    ic = IntCode(input_list.copy())
    ic.run()
    assert ic.output == 1125899906842624

    input_list = [
        109, -1, 4, 1, 99
    ]
    ic = IntCode(input_list.copy())
    ic.run()
    assert ic.output == -1

    input_list = [109, -1, 4, 1, 99]
    ic = IntCode(input_list.copy())
    ic.run()
    assert ic.output == -1
    input_list = [109, -1, 104, 1, 99]
    ic = IntCode(input_list.copy())
    ic.run()
    assert ic.output == 1
    input_list = [109, -1, 204, 1, 99]
    ic = IntCode(input_list.copy())
    ic.run()
    assert ic.output == 109
    input_list = [109, 1, 9, 2, 204, -6, 99]
    ic = IntCode(input_list.copy())
    ic.run()
    assert ic.output == 204
    input_list = [109, 1, 109, 9, 204, -6, 99]
    ic = IntCode(input_list.copy())
    ic.run()
    assert ic.output == 204
    input_list = [109, 1, 209, -1, 204, -106, 99]
    ic = IntCode(input_list.copy())
    ic.run()
    assert ic.output == 204
    input_list = [109, 1, 3, 3, 204, 2, 99]
    ic = IntCode(input_list.copy(), in_vals=[6854])
    ic.run()
    assert ic.output == 6854
    ic = IntCode(input_list.copy(), in_vals=[324538])
    ic.run()
    assert ic.output == 324538

test()
