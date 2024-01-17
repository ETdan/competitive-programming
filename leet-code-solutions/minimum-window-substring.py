class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        count_of_t=defaultdict(int)
        count_of_s=defaultdict(int)

        for char in t:
            count_of_t[char] += 1

        right=0
        left=0

        min_window_size=[9999,99999]

        answer=""

        def helper(count_of_t, count_of_s):
            for key,value in count_of_t.items():
                if key in count_of_s:
                    if count_of_s[key] < value:
                        return False
                else:
                    return False

            return True
        
        for right in range(len(s)):
            count_of_s[s[right]] += 1

            while left <= right and helper(count_of_t,count_of_s):
                # print(count_of_s,s[left:right+1],min_window_size,left,right,s[min_window_size[0]:min_window_size[1]])
                if min_window_size[1] - min_window_size[0] > right - left:
                    min_window_size=[left,right]

                if count_of_s[s[left]] > 1:
                    # print("here 1")
                    count_of_s[s[left]] -= 1
                else:
                    # print("here 2")
                    del count_of_s[s[left]]
                left+=1

        return s[min_window_size[0]:min_window_size[1]+1]