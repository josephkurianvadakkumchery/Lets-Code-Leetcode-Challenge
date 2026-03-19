class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid[0])
        
        for row in grid:
            left, right = 0, n - 1
            first_neg_idx = n 
            
            while left <= right:
                mid = (left + right) // 2
                if row[mid] < 0:
                    first_neg_idx = mid
                    right = mid - 1
                else:
                    left = mid + 1
            
            count += (n - first_neg_idx)
            
        return count
