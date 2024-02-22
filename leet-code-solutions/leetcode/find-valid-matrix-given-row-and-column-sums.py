class Solution:
    def restoreMatrix(self, rowsum: List[int], colsum: List[int]) -> List[List[int]]:
        grid = [[0]*len(colsum) for _ in range(len(rowsum))]
        m = len(rowsum)
        n = len(colsum)

        for i in range(m):
           
            grid[i][0]=rowsum[i]
        for i in range(n):
            cur_sum = 0
            target = colsum[i]

            for j in range(m):
                cur_sum+=grid[j][i]

                if cur_sum>target:
                    e = cur_sum-target
                    grid[j][i] -= e
                    grid[j][i+1] = e
                    cur_sum = target
        return grid
