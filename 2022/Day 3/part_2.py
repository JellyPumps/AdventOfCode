from itertools import islice

#files
testFile="inputs/test.txt"
inputFile="inputs/day_3_input.txt"

#variables
summ        =0

#dictionary
lowcase={
    "a":1,
    "b":2,
    "c":3,
    "d":4,
    "e":5,
    "f":6,
    "g":7,
    "h":8,
    "i":9,
    "j":10,
    "k":11,
    "l":12,
    "m":13,
    "n":14,
    "o":15,
    "p":16,
    "q":17,
    "r":18,
    "s":19,
    "t":20,
    "u":21,
    "v":22,
    "w":23,
    "x":24,
    "y":25,
    "z":26
}
highcase={
    "A":27,
    "B":28,
    "C":29,
    "D":30,
    "E":31,
    "F":32,
    "G":33,
    "H":34,
    "I":35,
    "J":36,
    "K":37,
    "L":38,
    "M":39,
    "N":40,
    "O":41,
    "P":42,
    "Q":43,
    "R":44,
    "S":45,
    "T":46,
    "U":47,
    "V":48,
    "W":49,
    "X":50,
    "Y":51,
    "Z":52
}

#read line by line
with open(inputFile) as file:
    #get items
    while True:
        rucksack=list(islice(file,3))
        if not rucksack:
            break
        f=[c for c in rucksack[0].rstrip()]
        s=[c for c in rucksack[1].rstrip()]
        t=[c for c in rucksack[2].rstrip()]
        priority=set(f).intersection(s,t)
        print(priority)
        for i in priority:
            if i.islower():
                summ+=lowcase[i]
            else:
                summ+=highcase[i]
        
print(summ)