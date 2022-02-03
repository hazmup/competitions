for T in range(int(input())):
    N = int(input())
    L = [int(x) for x in list(input().split())]
    l = len(L)
    cost = 0
    for i in range(1, l):
        for j in range(i-1, l):
            if L[j] == i:
                cost += j-i+2
                L[i-1:j+1] = L[-l+j:-l+i-2:-1]
    print('Case #{}: {}'.format(T+1,cost))
