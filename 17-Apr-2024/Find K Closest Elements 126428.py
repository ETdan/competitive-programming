# Problem: Find K Closest Elements - https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        num = bisect_left(arr,x)
       
        ans = []
        left = num - 1
        right = num
        while k:
            
            if left >= 0 and right < len(arr):
                if abs(arr[right] - x) >= abs(x - arr[left]):
                    ans.append(arr[left])
                    left -= 1
                else:
                    ans.append(arr[right])
                    right += 1
                
            elif left >= 0:
                ans.append(arr[left])
                left -= 1
            else:
                ans.append(arr[right])
                right += 1
            k -= 1
        
        ans.sort()
        return ans