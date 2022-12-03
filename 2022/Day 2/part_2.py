data=[]

#Read file column by column and append to list
with open("inputs/day_2_input.txt") as file:
    for line in file:
        data.append(line.rstrip())

totalScore=0
for i in range(len(data)):
    print(data[i])
    #Rock
    if data[i]=="A X":
        totalScore+=3
        print("Lose Case: ",totalScore)
    elif data[i]=="A Y":
        totalScore+=4
        print("Draw Case: ",totalScore)
    elif data[i]=="A Z":
        totalScore+=8
        print("Win Case: ",totalScore)
    #Paper
    elif data[i]=="B X":
        totalScore+=1
        print("Lose Case: ",totalScore)
    elif data[i]=="B Y":
        totalScore+=5
        print("Draw Case: ",totalScore)
    elif data[i]=="B Z":
        totalScore+=9
        print("Win Case: ",totalScore)
    #Scissors
    elif data[i]=="C X":
        totalScore+=2
        print("Lose Case: ",totalScore)
    elif data[i]=="C Y":
        totalScore+=6
        print("Draw Case: ",totalScore)
    elif data[i]=="C Z":
        totalScore+=7
        print("Win Case: ",totalScore)

#Debug
print(totalScore)

