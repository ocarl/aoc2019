def do_calc(input_list):
    gen = enumerate(input_list)
    for i, val in gen:
        if val == 1:
            val_a = input_list[input_list[i+1]]
            val_b = input_list[input_list[i+2]]
            # do add
            input_list[input_list[i+3]] = val_a + val_b
            for _ in range(3):
                next(gen)
        elif val == 2:
            val_a = input_list[input_list[i+1]]
            val_b = input_list[input_list[i+2]]
            # do multiply
            input_list[input_list[i+3]] = val_a * val_b
            for _ in range(3):
                next(gen)
        elif val == 99:
            return input_list
        else:
            continue
    return input_list


assert do_calc([1,0,0,0,99])[0] == 2
assert do_calc([2,3,0,3,99])[3] == 6
assert do_calc([2,4,4,5,99,0])[5] == 9801
assert do_calc([1,1,1,4,99,5,6,0,99])[0] == 30
assert do_calc([1,1,1,4,99,5,6,0,99])[4] == 2

if __name__ == '__main__':
    with open('input2.txt') as f:
        print(do_calc([int(x) for x in f.read().split(',')])[0])
