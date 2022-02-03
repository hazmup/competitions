col = {'U':(0,0,0), 'R':(1,0,0), 'Y':(0,1,0), 'B':(0,0,1), 'O':(1,1,0), 'P':(1,0,1), 'G':(0,1,1), 'A':(1,1,1)}
for case in range(int(input())):
    L = int(input())
    RGB = list(input().strip())
    result = 0
    R = [col[x][0] for x in RGB]
    Y = [col[x][1] for x in RGB]
    B = [col[x][2] for x in RGB]
    for i in [R,Y,B]:
        prev = 0
        for j in i:
            if (j == 1 and prev == 0):
                result += 1
            prev = j
    print('Case #{}: {}'.format(case+1,result))