# Problem: B - Excluded Integer Sum Problem - https://codeforces.com/gym/531455/problem/B

import sys
for _ in range(int(input())):
    n, k, x = map(int, sys.stdin.readline().strip().split())
    if x != 1:
    	print("YES")
    	print(n)
    	print(*([1] * n))
    elif k == 1 or (k == 2 and n % 2):
    	print("NO")

    else:
    	print("YES")
    	print(n // 2)
    		
    	print(*([2] * (n // 2 - 1)) + [3 if n % 2 == 1 else 2])