# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    bitn = ['0']
    bitn.extend(list(bin(n)[2:]))
    answer = ['0']*len(bitn)
    for i in range(len(bitn)-1, -1, -1):
        if bitn[i] == '1':
            answer[i] = '1'
            break

    if int(''.join(answer), 2) ^ int(''.join(bitn), 2) != 0:
        print(int(''.join(answer), 2))
    else:
        for i in range(len(bitn)-1, -1, -1):
            if bitn[i] == '0':
                answer[i] = '1'
                break
        print(int(''.join(answer), 2))
        # print(bitn)
        # print(answer)
