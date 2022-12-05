import re

aocdInp="2022/inputs/day_5_input.txt"
testInp="2022/inputs/test.txt"

stacks_count=[]; stacks_raw  =[]; stacks=[];
instructions=[];
raw         =[]

with open(aocdInp) as f:
    for line in f:
        raw.append(line.strip('\n'))
f.close()

blankIdx=raw.index('')
stacks_raw=raw[:blankIdx]; instructions=raw[blankIdx+1:]

#PARSE STACKS
stacks_count.append(stacks_raw.pop(-1)); stacks_count=[x.strip(' ') for x in stacks_count]
stacks_count[0]=re.sub(re.compile(r'\s+'),',',stacks_count[0])
stacks_count=[item.split(',') for item in stacks_count]
stacks_count=[item for l in stacks_count for item in l]
for i in range(len(stacks_count)):
    stacks_count[i]=int(stacks_count[i])
noStacks=stacks_count[-1]
for i in range(len(stacks_raw)):
    stacks_raw[i]=[stacks_raw[i][x:x+noStacks] for x in range(0,len(stacks_raw[i]),noStacks-2)]
for i in range(noStacks):
    app=[x[i] for x in stacks_raw]
    stacks.append(app)
for i in range(len(stacks)):
    for y in range(len(stacks[i])):
        stacks[i][y]=re.sub(re.compile(r'\s+'),'',stacks[i][y])
    stacks[i]=[x for x in stacks[i] if x]

#PARSE INSTRUCTIONS
for i in range(len(instructions)):
    instructions[i]=re.sub('[^0-9]','',instructions[i])

#REARRANGE
for i in range(len(instructions)):
    numberToMove=int(instructions[i][0])
    moveFromStck=int(instructions[i][1])-1
    stckDestintn=int(instructions[i][2])-1

    print(moveFromStck)

    for x in range(numberToMove):
        targ=stacks[moveFromStck]        
        dest=stacks[stckDestintn]
        dest.insert(0,targ[0])
        targ.pop(0)

for i in range(len(stacks)):
    print(*stacks[i][0],sep='',end='')

#print(stacks)
print()
print("Number of stacks:",noStacks)