# Problem: Thearte Square - https://codeforces.com/problemset/problem/1/A

from math import ceil
n, m, a = list(map(int, (input().split())))
left = ceil(n/a)
right = ceil(m/a)
 
print(left*right)