# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        children = [0] * k 
        min_unfairness = float("inf")

        def backTrack(i):
            nonlocal min_unfairness

            if i == len(cookies):
                unfair = max(children)
                min_unfairness = min(min_unfairness, unfair)
                return

            for j in range(k):
                children[j] += cookies[i]
                if children[j] < min_unfairness:
                    backTrack(i + 1)
                children[j] -= cookies[i]

        backTrack(0)

        return min_unfairness
