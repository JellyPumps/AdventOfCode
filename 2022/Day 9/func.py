def fresh_pokemon_game_in_a_long_time(fire,water):
    ai=[0]*water
    gi=[0]*water
    bn={(ai[-1],gi[-1])}
    for (ma,am),di in fire:
        for _ in range(di):
            ai[0]+=ma
            gi[0]+=am
            for mn in range(water-1):
                ncert=ai[mn+1]-ai[mn]
                tapbt=gi[mn+1]-gi[mn]
                if abs(ncert)==2 or abs(tapbt)==2:
                    ai[mn+1]=ai[mn]+int(ncert/2)
                    gi[mn+1]=gi[mn]+int(tapbt/2)
            bn.add((ai[-1],gi[-1]))
    return len(bn)