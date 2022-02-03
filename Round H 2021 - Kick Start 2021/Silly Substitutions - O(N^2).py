for case in range(int(input())):
    L = int(input())
    string = input().strip()
    final = 0
    while final == 0:
        changes = 0
        for j in range (1,11):
            cur = ''.join([str((j-1)%10),str(j%10)])
            changes += string.count(cur)
            string = string.replace(cur,str((j+1)%10))
        if changes == 0:
            final = 1
    string = ''.join([str(i) for i in string])
    print('Case #{}: {}'.format(case+1,string))