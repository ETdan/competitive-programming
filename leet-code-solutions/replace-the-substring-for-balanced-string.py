class Solution:
    def balancedString(self, s: str) -> int:
        count_s = defaultdict(int)
        min_len =float('inf')
        been_here = False

        def need_is_in_there(needed_window, counter):
            # print("here", needed_window, counter)
            if len(needed_window) == 0 or len(counter) == 0:
                return False
            for key, val in needed_window.items():
                if key in counter:
                    if counter[key] < val:
                        return False
                    else:
                        continue
                else:
                    return False
            return True

        for i in range(len(s)):
            count_s[s[i]] += 1

        needed_window = defaultdict(int)

        for key, val in count_s.items():
            if val > len(s) // 4:
                needed_window[key] = val - len(s) // 4

        # search for the needed window
        left = 0
        counter = defaultdict(int)
        for right in range(len(s)):
            counter[s[right]] += 1
            # print(counter,needed_window)
            while left < len(s) and need_is_in_there(needed_window, counter):
                # print(left)
                been_here = True
                if counter[s[left]] > 1:
                    counter[s[left]] -= 1
                else:
                    del counter[s[left]]

                # if need_is_in_there(needed_window, counter):
                min_len = min(right - left + 1, min_len)
                left += 1

        return 0 if not been_here else min_len
