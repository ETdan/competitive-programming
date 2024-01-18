class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if k == len(s):
            return k
        counter = defaultdict(int)
        left = 0

        def helper(counter):
            max_ = 0
            for key, val in counter.items():
                if val > max_:
                    max_ = val
            return max_

        max_len = k

        for i in range(k):
            counter[s[i]] += 1

        for right in range(k, len(s)):
            counter[s[right]] += 1
            while right - left + 1 - helper(counter) > k:
                # print(left,right,s[right],helper(counter))
                if counter[s[left]] > 1:
                    counter[s[left]] -= 1
                else:
                    del counter[s[left]]
                left += 1

            max_len = max( right - left + 1,max_len)

        return max_len
