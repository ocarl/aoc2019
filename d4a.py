def valid_pass(num):
    numstr = str(num)
    if len(numstr) > 6:
        return False
    found_duplicates = False
    iter_str = iter(numstr)
    iter_str2 = iter(numstr)
    _ = next(iter_str2)
    for digit in iter_str:
        try:
            next_digit = next(iter_str2)
        except StopIteration:
            return found_duplicates
        if digit > next_digit:
            return False
        if len(numstr.replace(digit, '')) <= 4:
            found_duplicates = True
    return found_duplicates


assert valid_pass(111111)
assert not valid_pass(223450)
assert not valid_pass(123789)
assert valid_pass(266669)

passing = []
for x in range(265275, 781585):
#for x in range(265275, 266669):
    if valid_pass(x):
        passing.append(x)

print(len(passing))

