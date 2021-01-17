from sys import stdin
l = list(map(int, stdin.read().split()))
print((l[0] * (l[1] + 1)) - sum(l[2:]))