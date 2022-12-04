from collections.abc import Iterable
aocdInp  = open("2022/inputs/day_4_input.txt")
testInp  = open("2022/inputs/test.txt")
ovrcnt=0
rnovrcnt=0
inlist=[]
flatten = lambda *n: (e for a in n for e in (flatten(*a) if isinstance(a, (tuple, list)) else (a,)))

while True:
    line=aocdInp.readline()
    if not line: break
    x=[int(i)  for i in line.split(',')[0].split('-')]; y=[int(i)  for i in line.split(',')[1].split('-')]
    for s in range(x[0]+1,x[1]): x.append(s)
    for s in range(y[0]+1,y[1]): y.append(s)
    if set(y).issubset(set(x)) or set(x).issubset(y):ovrcnt+=1
    for s in x:
        if s in y: rnovrcnt+=1; break

print(ovrcnt)
print(rnovrcnt)
aocdInp.close()

        