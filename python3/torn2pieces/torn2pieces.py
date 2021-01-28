from sys import stdin 
num_lines = int(stdin.readline())

# Make a dictionary class that has an initialized 
# value everytime
def initialized_set_dict():
    class InitDict(dict):
        def __getitem__(self, key):
            if key not in self:
                dict.__setitem__(self, key, set())
            return dict.__getitem__(self, key)
    return InitDict()

locations_map = initialized_set_dict()

for _ in range(num_lines):
    loc = stdin.readline().split()
    for trailing_locs in loc[1:]:
        locations_map[loc[0]].add(trailing_locs)
        locations_map[trailing_locs].add(loc[0])

initial, final = input().split()
visited = set(list(initial))

remaining_locs = []
for loc in locations_map[initial]:
    addresses = initial, loc
    remaining_locs.append((loc, [*addresses]))

while remaining_locs and final != remaining_locs[0][0]:
    s, track = remaining_locs.pop(0)
    if s not in visited:
        visited.add(s)
        for c in locations_map[s] - visited:
            remaining_locs.append((c, track + [c]))
print(" ".join(remaining_locs[0][1])) if remaining_locs\
    else print("no route found")