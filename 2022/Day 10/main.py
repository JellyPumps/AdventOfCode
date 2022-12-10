from comp import *
test="2022/inputs/test.txt"
aocd="2022/inputs/day_10_input.txt"
target=test
with open(target) as f:
    for line in f:
        line=line.rstrip()
        cont=line.split()
        if cont[0]=='noop': noop()
        if cont[0]=='addx': addx(int(cont[1]))
peepee()