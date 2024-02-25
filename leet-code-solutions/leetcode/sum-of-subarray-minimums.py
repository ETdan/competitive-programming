class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        answer = 0
        stack = []

        for i in range(len(arr)):
            while stack and arr[i] < arr[stack[-1]]:
                j = stack.pop()
                left = j - stack[-1] if stack else j + 1
                right = i - j
                answer += (arr[j] * left * right)
            stack.append(i)

        for i in range(len(stack)):
            left = stack[i] - stack[i - 1] if i > 0 else stack[i] + 1
            right = len(arr) - stack[i]
            answer += (arr[stack[i]] * left * right) 

        return answer % (10**9 + 7)
