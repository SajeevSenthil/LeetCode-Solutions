class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        start= 0
        end = m*n - 1   
        while start <= end:
            mid = (start + end) // 2
            mid_value = matrix[mid // n][mid % n] 
            if mid_value == target:
                return True  
            elif mid_value < target:
                start = mid + 1
            else:
                end = mid - 1  
        return False 
