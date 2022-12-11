test="2022/inputs/test.txt"
aocd="2022/inputs/day_10_input.txt"
target=aocd
cycles=1
regx  =1
signal=0
catch =[20,60,100,140,180,220]
wonder=[]

def sumeru()->None:
    global cycles,signal,regx
    if cycles in catch: signal+=cycles*regx
    else              : 0
with open(target) as f:
    for line in f:
        line=line.rstrip()
        wonder.append(line)
        cycles+=1
        if 'addx' in line:
            sumeru()
            cycles+=1
            regx+=int(line.split()[1])
        sumeru()
f.close()

regx  =1
cycles=0
pepsi=lambda cycles,regx: '■' if abs(cycles-regx)<=1 else '◦'
crt=''
tond=[]

for i in wonder:
    crt+=pepsi(cycles,regx); cycles=(cycles+1)%40
    if 'addx' in i:
        crt+=pepsi(cycles,regx)
        cycles=(cycles+1)%40
        regx+=int(i.split()[1])
print(f"Part 1: {signal}")
for row in range(0,6): print(crt[row*40:(row+1)*40])


