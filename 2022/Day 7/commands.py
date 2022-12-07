from collections import defaultdict
#init base directory variables
struc=[]
fsize=defaultdict(int)
#0=directory change, 1=list
def parse_commands(item:str):
    global struc
    match item.split():
        case ['$','cd','/'  ] : pass
        case ['$','cd','..' ] : struc.pop();
        case ['$','cd', di  ] : struc.append(di)
        case ['$','ls'      ] : pass
        case ['dir',suchpain] : pass
        case [size,file     ] : parse_item(size,file)
def parse_item(size:str,file:str):
    global fsize;
    fsize[tuple(struc)]+=int(size)
    path=struc[:-1]
    while path: fsize[tuple(path)]+=int(size); path.pop()

