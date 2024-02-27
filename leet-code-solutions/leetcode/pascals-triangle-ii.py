class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        Dict = defaultdict(int)

        def recur(r, index):
            if (r, index) in Dict:
                return Dict[(r,index)]
            if r < index:
                return 0
            if r == 1 or index == 0:
                return 1

            r1 = recur(r - 1, index - 1)
            r2 = recur(r - 1, index)
            Dict[(r - 1, index - 1)] = r1
            Dict[(r - 1, index)] = r2

            return r1 + r2

        answer = []
        for i in range(rowIndex + 1):
            answer.append(recur(rowIndex, i))
            

        return answer


"""
if (r,index) in [(1,0),(1,1),(0,0)]:
                return 1
            elif (r,index) in ((1,2),(0,1),(0,2)):
                return 0
"""
