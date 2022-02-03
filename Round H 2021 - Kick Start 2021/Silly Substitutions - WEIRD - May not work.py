for case in range(int(input())):
    L = int(input())
    string = [int(x) for x in list(input())]
    final = 0
    while final == 0:
        changes = 0
        for j in range (1,11):
            for i in range(1,len(string)):
                if string[i]%10==(string[i-1]+1)%10==j%10:
                    string[i-1:i+1] = [(j+1)%10]
                    changes += 1
                    break
            if changes >0:
                break
        if changes == 0:
            final = 1
    string = ''.join([str(i) for i in string])
    print('Case #{}: {}'.format(case+1,string))