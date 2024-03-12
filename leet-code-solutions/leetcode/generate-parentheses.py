class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = ""
        res = []

        def backtrack(openCount, closeCount, stack, res, n):
            if len(stack) == n * 2:
                res.append(stack)
                return
            
            if openCount < n:
                backtrack(openCount + 1, closeCount, stack + "(", res, n)
            if closeCount < openCount:
                backtrack(openCount, closeCount + 1, stack + ")", res, n)

        backtrack(0, 0, stack, res, n)       
            
        return res