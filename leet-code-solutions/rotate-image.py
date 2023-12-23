class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left,right = 0,(len(matrix)-1)
        
        while left < right:
            for i in range(right-left):
                top,bottom = left,right

                lefttop = matrix[top][left + i]
                
                # left-bottom to left-top
                matrix[top][left + i] = matrix[bottom - i][left]
                
                # right-bottom to left-bottom
                matrix[bottom - i][left]  =  matrix[bottom][right - i]
                
                # right-top to bottom-right
                matrix[bottom][right - i] = matrix[top + i][right]

                # left-top to top-right
                matrix[top + i][right] = lefttop
            left+=1
            right-=1