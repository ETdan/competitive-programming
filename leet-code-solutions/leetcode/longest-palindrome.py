class Solution:
    def longestPalindrome(self, s: str) -> int:
        Dict = defaultdict(int)

        have_single_char = False

        for i in range(len(s)):
            Dict[s[i]] += 1

        lenn = 0

        if len(Dict) == 1:
            return len(s)

        for key, val in Dict.items():
            if val == 1 and not have_single_char:
                lenn += 1
                have_single_char = True
            else:
                if val % 2 ==0:
                    lenn += val
                else:
                    if not have_single_char:
                        lenn += val
                        have_single_char = True
                
                    else:
                        lenn += (val-1)

        return lenn
