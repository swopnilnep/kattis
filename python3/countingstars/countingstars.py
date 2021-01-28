from sys import setrecursionlimit, stdin
setrecursionlimit(10 ** 4)

def remove(items, x, y):
    if items[x][y]:
        items[x][y] = False
        for i, j in ((0, 1),(0,-1),(1, 0),(-1, 0)):
            x_mod, y_mod = x + i, y + j
            if not any((x_mod < 0,\
                y_mod < 0,\
                x_mod >= len(items),\
                y_mod >= len(items[0]))): items = remove(items, x_mod, y_mod)
    return items

for row_num, meta in enumerate(stdin):
    x_axis, y_axis = map(int, meta.split())
    is_star = [[False for x in range(y_axis)] for x in range(x_axis)]
    for l in range(x_axis):
        line = stdin.readline()
        for star in range(y_axis):
            if line[star] == "-": is_star[l][star] = True
    count = 0
    not_visited = list(range(len(is_star)))
    while len(not_visited) > 0:
        for x in not_visited:
            line = is_star[x]
            if True in line:
                y = line.index(True)
                is_star = remove(is_star, x, y)
                count += 1
            else:
                not_visited.remove(x)
                continue
    
    print(f"Case {row_num + 1}: {count}")