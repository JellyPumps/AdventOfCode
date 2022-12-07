import commands as cmd

test="2022/inputs/test.txt"
aocd="2022/inputs/day_7_input.txt"

cmds=[]

#0=directory change, 1=list

with open(aocd) as file:
    for line in file:
        cmds.append(line.rstrip())
file.close()
for command in cmds: cmd.parse_commands(command)

print("Part 1:",sum([s for s in cmd.fsize.values() if s<=100000]))
freespace=70000000-cmd.fsize[('/')]
print("Part 2:",min([s for s in cmd.fsize.values() if s+freespace>=30000000]))
