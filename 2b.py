from d2a import do_calc

with open('input2.txt') as f:
    inlist = [int(x) for x in f.read().split(',')]
    for noun in range(100):
        for verb in range(100):
            inlist_c = inlist.copy()
            inlist_c[2] = verb
            inlist_c[1] = noun
            try:
                result = do_calc(inlist_c)
            except:
                continue
            if result[0] == 19690720:
                print(100 * noun + verb)
