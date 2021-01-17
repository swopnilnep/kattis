import sys

# Formula
# (r1 + r2) / 2 = S
# r1 + r2 = 2s
# r2 = 2s - r1

def find_r2(r1:int, s:int) -> int:
    return 2 * s - r1

def main():
    r1,s =  (int(x) for x in sys.stdin.readline().strip().split())
    print(find_r2(r1,s))

main()