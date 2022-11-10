ixes = ygreks = zets = [0, 1]
for x in ixes:
    for y in ygreks:
        for z in zets:
            print(f'{x} {y} {z}  -  {not (x or y or z) == (not x) and (not y) and (not z)}')
