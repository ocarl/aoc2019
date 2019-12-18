from intcode import IntCode

with open('input9.txt') as f:
    ic = IntCode([int(x) for x in f.read().split(',')], in_vals=[2])
    output = []
    while not ic.stopped:
        ic.run()
        output.append(ic.output)
    print(output)
