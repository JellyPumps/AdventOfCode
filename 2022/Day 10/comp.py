catch=20
regx=1
cycl=0
cinst=''
pinst=''
signal=0
def step()->None:
    global regx,cycl,cinst,signal,catch,prev
    if catch>220: catch=220
    temp=0
    if cycl==catch:
        temp=cycl*regx
        signal+=temp
        catch+=40
    cycl+=1
    print(f'Cycle: {cycl},X: {regx}, CI: {cinst},S: {signal}, C: {catch}, T: {temp}')
def addx(v)->None:
    global regx,cinst,prev
    cinst=f'addx {v}'
    for _ in range(2): step()
    regx+=v
def noop()->None:
    global cycl,cinst
    cinst='noop'
    step()
def peepee()->None:
    global signal
    print(signal)