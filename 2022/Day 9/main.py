from func import *
test="2022/inputs/test.txt"
aocd="2022/inputs/day_9_input.txt"
target=aocd
direc={'L':(-1,0),'R':(1,0),'D':{0,-1},'U':(0,1)}
instr=[(direc[line[0]],int(line[1:])) for line in open(target)]
result1=str(fresh_pokemon_game_in_a_long_time(instr,2))
result2=str(fresh_pokemon_game_in_a_long_time(instr,10))
print('Part 1:',result1)
print('Part 2:',result2)