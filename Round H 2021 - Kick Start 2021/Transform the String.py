for case in range(int(input())):
    S = [ord(x)-ord('a') for x in list(input().strip())]
    F = [ord(x)-ord('a') for x in list(input().strip())]
    result = 0
    dist = {}
    for s in S:
        if s not in dist:
            dist[s] = min(min(abs(s-f),26-abs(s-f)) for f in F)
        result += dist[s]
    print('Case #{}: {}'.format(case+1,result))