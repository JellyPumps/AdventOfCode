#Set values
A="ROCK"; B="PAPER"; C="SCISSORS"
ROCK,PAPER,SCISSORS=1,2,3
LOSE_CASE,DRAW_CASE,WIN_CASE=0,3,6

#Read file column by column and append to list
with open("inputs/day_2_input.txt") as file:
    data=[line.strip().split() for line in file.readlines()]
col_1=[record[0] for record in data]
col_2=[record[1] for record in data]

#Turn values to readable values
def replaceVal(repl):
    for i in range(len(repl)):
        if repl[i]=="A" or repl[i]=="X":
            repl[i]=A
        elif repl[i]=="B" or repl[i]=="Y":
            repl[i]=B
        elif repl[i]=="C" or repl[i]=="Z":
            repl[i]=C

#Compare

roundScore=[]

def compare(colm,ccollmm):
    totalScore=0
    for f in range(len(colm)):
        for o in range(len(ccollmm)):
            shapeScore=0
            outcomeScore=0
            #set shapeScore
            if ccollmm[o]==A:
                    shapeScore=ROCK
            elif ccollmm[o]==B:
                    shapeScore=PAPER
            elif ccollmm[o]==C:
                    shapeScore=SCISSORS
            #set outcomeScore
            if ccollmm[o]==colm[1]:
                outcomeScore=DRAW_CASE
                
            elif ccollmm[o]==A:
                if colm[f]==C:
                    outcomeScore=WIN_CASE
                else:
                    outcomeScore=LOSE_CASE
            elif ccollmm[o]==B:
                if colm[f]==A:
                    outcomeScore=WIN_CASE
                else:
                    outcomeScore=LOSE_CASE
            elif ccollmm[o]==C:
                if colm[f]==B:
                    outcomeScore=WIN_CASE
                else:
                    outcomeScore=LOSE_CASE
            score=outcomeScore+shapeScore
            roundScore.append(score)
replaceVal(col_1)
replaceVal(col_2)

compare(col_1,col_2)

totalScore=sum(roundScore)

#Debug
print(totalScore)

