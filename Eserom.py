map = {}
with open('Eserom_map.txt', 'r') as f:
    while ln := f.readline():
        data = ln.split(' ')
        map[data[0]] = data[1]


for char in input().split(' '):
    print(map[char], end='')
