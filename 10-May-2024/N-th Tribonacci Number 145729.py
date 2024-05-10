# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    Dict = defaultdict(int)
    Dict[0]=0
    Dict[1]=1
    Dict[2]=1
    
    def tribonacci(self, n: int) -> int:
        if n in self.Dict:
            return self.Dict[n]

        answer = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        self.Dict[n] = answer
        return answer
