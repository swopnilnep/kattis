import sys
dmap = {}
rmap = {}
for line in sys.stdin.readlines():
    tkns = line.strip().split()
    if tkns[0] == 'def':
        n = tkns[1]
        val = int(tkns[2])
        if n in dmap:
            del rmap[dmap[n]]
            del dmap[n]
        dmap[n] = val
        rmap[val] = n
    elif tkns[0] == 'clear':
        dmap = {}
        rmap = {}
    else:
        cmd = ' '.join(tkns[1:])
        tkns[0] = '+'
        tkns = tkns[:-1]
        ans = 0
        for i in range(0, len(tkns), 2):
            sign = tkns[i]
            val = tkns[i + 1]
            if val not in dmap.keys():
                ans = ''
                break
            ans += (1 if sign == '+' else -1) * dmap[val]
        print(cmd, rmap.get(ans, 'unknown'))