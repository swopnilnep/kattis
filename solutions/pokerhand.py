from sys import stdin
r = stdin.readline()[0::3]
m = [r.count(c) for c in set(r)]
print(max(m))