class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        last_index = {}
        right = 0
        min_len = float("inf")

        for right in range(len(cards)):
            if cards[right] in last_index:
                min_len = min(min_len, right - last_index[cards[right]] + 1)

            last_index[cards[right]]=right

        return -1 if min_len == float("inf") else min_len
