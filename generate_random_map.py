import random

SHOP_NUM = 2 # per player
MAP_CONFIG_ID = 4

map_data = [['0' for i in range(25)] for j in range(20)]

for s in ['w', 's', 'm']:
    for i in range(SHOP_NUM):
        x = random.randint(0,19)
        y = random.randint(0,24)
        while (x == 0 and y == 0):
            x = random.randint(0,19)
            y = random.randint(0,24)

        map_data[x][y] = s
        map_data[19-x][24-y] = s


file_map = open('server_jar/maps/mapConfig' + str(MAP_CONFIG_ID) + '.txt', 'w')

file_map.writelines(list(map(lambda lst: "".join(lst) + '\n', map_data)))


