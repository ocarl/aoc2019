class IntCode:
    def __init__(self, input_list, in_vals=[]):
        self.program = input_list
        self.output = None
        self.input = in_vals
        self.gen = enumerate(self.program)
        self.stopped = False

    def reset(self):
        self.gen = enumerate(self.program)

    def run(self):
        self.input = iter(self.input)
        while True:
            i, val = next(self.gen)
            op_code = val % 100
            param1_mode = int((val - op_code) % 1000 / 100)
            param2_mode = int((val - op_code - param1_mode) % 10000 / 1000)
            param3_mode = int(
                (val - op_code - param1_mode - param2_mode) % 100000 / 10000)
            if any(map(lambda x: x > 1, [param1_mode, param2_mode, param3_mode])):
                continue
            if op_code == 1:
                # add
                param_mode_list = [(self.program[i + 1], param1_mode),
                                   (self.program[i + 2], param2_mode),
                                   (self.program[i + 3], param3_mode)]
                self.operator(param_mode_list, fun=lambda x, y: x + y)
                for _ in range(len(param_mode_list)):
                    next(self.gen)
            elif op_code == 2:
                # multiply
                param_mode_list = [(self.program[i + 1], param1_mode),
                                   (self.program[i + 2], param2_mode),
                                   (self.program[i + 3], param3_mode)]
                self.operator(param_mode_list, fun=lambda x, y: x * y)
                for _ in range(len(param_mode_list)):
                    next(self.gen)
            elif op_code == 3:
                # read input
                param = self.program[i + 1]
                self.program[param] = next(self.input)
                for _ in range(1):
                    next(self.gen)
            elif op_code == 4:
                # write output
                param = self.program[i + 1]
                mode = param1_mode
                if mode == 0:
                    self.output = self.program[param]
                if mode == 1:
                    self.output = param
                for _ in range(1):
                    next(self.gen)
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
                    next(self.gen)
            elif op_code == 8:
                # equals
                param_mode_list = [(self.program[i + 1], param1_mode),
                                   (self.program[i + 2], param2_mode),
                                   (self.program[i + 3], param3_mode)]
                self.store_bool(param_mode_list, comp=lambda x, y: x == y)
                for _ in range(len(param_mode_list)):
                    next(self.gen)
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
        return operands

    def operator(self, param_mode_list, fun=lambda x, y: x + y):
        operands = self._parse_operands(param_mode_list[:-1])
        operands.append(param_mode_list[-1][0])
        self.program[operands[-1]] = fun(*operands[:-1])

    def jump(self, param_mode_list, comp=lambda x: x != 0):
        operands = self._parse_operands(param_mode_list)
        if comp(operands[0]):
            self.gen = enumerate(self.program)
            for _ in range(operands[1]):
                next(self.gen)

    def store_bool(self, param_mode_list, comp=lambda x, y: x < y):
        operands = self._parse_operands(param_mode_list[:-1])
        operands.append(param_mode_list[-1][0])
        if comp(operands[0], operands[1]):
            self.program[operands[2]] = 1
        else:
            self.program[operands[2]] = 0


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
    assert ic.output == 1
    ic = IntCode(input_list, in_vals=[0])
    ic.run()
    assert ic.output == 0

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


test()
