string="bvwbjplbgvbhsrlpgdmjqwftvncz"
spliced=[]
processed=0
count=0

with open("2022/inputs/day_6_input.txt") as file:
    while True:
        c=file.read(1)
        if not c:
            break
        spliced.append(c)
for c in range(len(spliced)):
    s=spliced
    try: temp=[s[c],s[c+1],s[c+2],s[c+3]]
    except IndexError as e: print(e); exit()
    tmpstr=""
    for e in temp:
        tmpstr+=e
    if len(set(tmpstr))==len(tmpstr):
        processed=3+1+count; break
    count+=1

print(processed)