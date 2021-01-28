from sys import stdin

WEEK_MINS = 10080
LAWN_SIZE, OWNERS = (int(x) for x in stdin.readline().split())
parts = []

def main():
    for idx in range(OWNERS):
        name, *spec = stdin.readline().split(",")
        spec = tuple(int(x) for x in spec)
        total = WEEK_MINS * spec[1] * spec[2] // (spec[2] + spec[3])
        if total >= LAWN_SIZE: parts.append((spec[0], idx, name))
    if len(parts) > 0:
        parts.sort()
        mower = parts[0][0]
        for p in parts:
            if p[0] == mower: print(p[-1])
    else: print("no such mower")            

if __name__ == "__main__":
    main()