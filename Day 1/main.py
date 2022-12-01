from more_itertools import split_at

group=[]

#Open and read
with open("input.txt") as file:
    for line in file:
        group.append(line)

#Subdivde `group` into sub lists by new line
dividedgroup=[
    [item.rstrip() for item in sublist]
    for sublist in split_at(group, lambda i: i=='\n')
    if sublist
]

#Turn numbers from string to int
def convert_to_int(lists):
  return [int(el) if not isinstance(el,list) else convert_to_int(el) for el in lists]
intgroup=convert_to_int(dividedgroup)

#Add all numbers in sublists
sumgroup=[sum(x) for x in intgroup]

#Find largest number in final list
sumgroup.sort()
print("The most amount calories an Elf is carrying is: ",sumgroup[-1])

#Part 2
print("Total calories between top 3: ",sumgroup[-1]+sumgroup[-2]+sumgroup[-3])