from sys import stdin
i = int(stdin.readline())
if (i > 0):
    out = "Alice" if (i % 2 == 1) else "Bob"
    print(out)