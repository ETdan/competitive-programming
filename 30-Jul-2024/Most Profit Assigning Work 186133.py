# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        dif_pro = list(zip(difficulty, profit))
        dif_pro.sort()
        worker.sort()

        p = x = i = 0

        for w in worker:
            while i < len(worker) and w >= dif_pro[i][0]:
                x = max(x, dif_pro[i][1])
                i+=1

            p += x

        return p
