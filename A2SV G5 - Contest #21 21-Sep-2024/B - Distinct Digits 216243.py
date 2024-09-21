# Problem: B - Distinct Digits - https://codeforces.com/gym/530187/problem/B

T = int(input())

for _ in range(T):
    n = int(input())

    ans = []
    for digit in range(9, 0, -1):
        if n >= digit:
            ans.append(digit)
            n -= digit
    ans.reverse()
    print(*ans, sep="")