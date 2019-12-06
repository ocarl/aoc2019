class IntCode:
    def __init__(self, input_list):
        self.program = input_list
        self.output = None

    def run(self):
        gen = enumerate(self.program)
        for i, val in gen:
            op_code = val%100
            param1_mode = int((val-op_code)%1000/100)
            param2_mode = int((val-op_code-param1_mode)%10000/1000)
            param3_mode = int((val-op_code-param1_mode-param2_mode)%100000/10000)
            if op_code == 1:
                param_mode_list=[(self.program[i+1], param1_mode),
                                 (self.program[i+2], param2_mode),
                                 (self.program[i+3], param3_mode)]
                self.operator(param_mode_list, fun=lambda x, y: x+y)
                for _ in range(3):
                    next(gen)
            elif op_code == 2:
                param_mode_list=[(self.program[i+1], param1_mode),
                                 (self.program[i+2], param2_mode),
                                 (self.program[i+3], param3_mode)]
                self.operator(param_mode_list, fun=lambda x, y: x*y)
                for _ in range(3):
                    next(gen)
            elif op_code == 3:
                param_mode_list=[(self.program[i+1], param1_mode),
                                 (self.program[i+2], param2_mode)]
                self.operator(param_mode_list, fun=lambda x: x)
                for _ in range(2):
                    next(gen)
            elif op_code == 4:
                param = self.program[i+1]
                mode = param1_mode
                if mode == 0:
                    self.output = self.program[param]
                if mode == 1:
                    self.output = param
                for _ in range(1):
                    next(gen)
            elif op_code == 99:
                return self.program
            else:
                continue

    def operator(self, param_mode_list, fun=lambda x, y: x + y):
        operands = []
        for param, mode in param_mode_list[:-1]:
            if mode == 0:
                operands.append(self.program[param])
            if mode == 1:
                operands.append(param)
        operands.append(param_mode_list[-1][0])

        self.program[operands[-1]] = fun(*operands[:-1])


def test():
    input_list = [1002, 4, 3, 4, 33]
    ic = IntCode(input_list)
    ic.run()
    assert ic.program[-1] == 99

test()

if __name__ == '__main__':
    with open('input5.txt') as f:
        ic = IntCode([int(x) for x in f.read().split(',')])
        ic.run()
        print(ic.output)