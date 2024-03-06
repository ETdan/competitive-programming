class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        left = -1
        right = len(letters) - 1

        mid = (left + right) // 2
        smallest_great_char = "z"

        while (left +1) < right:
            # print(left,right,mid)
            if letters[mid] <= target:
                left = mid
            else:
                right = mid

            mid = (left + right) // 2

        return letters[right] if letters[right] > target else min(letters)
