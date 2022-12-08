import numpy as np

test="2022/inputs/test.txt"
aicunjiern="2022/inputs/day_8_input.txt"

skymap=np.array([list(no.strip()) for no in open(aicunjiern)],int)
tvrnhjONE=np.zeros_like(skymap,int)
pocmndTWO=np.ones_like(skymap,int)

for rr in range(4):
    for axe,yoodle in np.ndindex(skymap.shape):
        low=[tree<skymap[axe,yoodle] for tree in skymap[axe,yoodle+1:]]
        tvrnhjONE[axe,yoodle]|=all(low)
        pocmndTWO[axe,yoodle]*=next((cj+1 for cj,bigsmoke in enumerate(low) if ~bigsmoke),len(low))
    skymap,tvrnhjONE,pocmndTWO=map(np.rot90,[skymap,tvrnhjONE,pocmndTWO])
tvrnhjONE=tvrnhjONE.sum()
pocmndTWO=pocmndTWO.max()
print(tvrnhjONE)
print(pocmndTWO)