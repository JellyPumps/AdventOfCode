#Set values
LOSE_CASE,DRAW_CASE,WIN_CASE=0,3,6

data=[]

#Read file column by column and append to list
with open("inputs/day_2_input.txt") as file:
    for line in file:
        data.append(line.rstrip())

totalScore=0
for i in range(len(data)):
    print(data[i])
    if data[i]=="A X" or data[i]=="B Y" or data[i]=="C Z":
        totalScore+=DRAW_CASE
        print("Draw Case: ",totalScore)
    elif data[i]=="A Y" or data[i]=="B Z" or data[i]=="C X":
        totalScore+=WIN_CASE
        print("Win Case: ",totalScore)
    else:
        totalScore+=LOSE_CASE
        print("Lose Case: ",totalScore)
    if "X" in data[i]:
        totalScore+=1
        print("Rock: ",totalScore)
    elif "Y" in data[i]:
        totalScore+=2
        print("Paper: ",totalScore)
    elif "Z" in data[i]:
        totalScore+=3
        print("Scissors: ",totalScore)

#Debug
print(totalScore)

