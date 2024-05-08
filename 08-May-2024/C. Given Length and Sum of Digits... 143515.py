# Problem: C. Given Length and Sum of Digits... - https://codeforces.com/contest/489/problem/C

import sys
input = sys.stdin.readline
m, s = list(map(int, input().split()))
arr = list(map(int, input().split()))

if s != 0 or m < 2:
    min_answer = [0]*m
    max_answer = [0]*m

    smin = s-1
    smax = s

    mmin = m-1
    mmax = 0

    if s >= 1:
        min_answer[0] = 1

    while smin > 0 and mmin >= 0:
        if smin - 9 > 0:
            min_answer[mmin] = 9
            smin -= 9
        else:
            if min_answer[mmin] + smin > 9:
                min_answer = -1
            else:
                min_answer[mmin] += smin

            smin = 0

        mmin -= 1
    if smin > 0:
        min_answer = -1

    while smax > 0 and mmax < m:
        if smax - 9 > 0:
            max_answer[mmax] = 9
            smax -= 9
        else:
            if max_answer[mmax] + smax > 9:
                max_answer = -1
            else:
                max_answer[mmax] += smax

            smax = 0

        mmax += 1

    if smax > 0:
        max_answer = -1

    ans1 = []
    ans2 = []

    if min_answer != -1:
        ans1 = []
        for num in min_answer:
            ans1.append(str(num))
        ans1 = ''.join(ans1)
    else:
        ans1 = -1

    if max_answer != -1:
        ans2 = []
        for num in max_answer:
            ans2.append(str(num))
        ans2 = ''.join(ans2)
    else:
        ans2 = -1

    print(ans1, ans2)
else:
    print(-1, -1)
