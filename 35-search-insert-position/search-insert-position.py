class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Initialize search boundaries
        left, right = 0, len(nums) - 1
        
        # Perform binary search
        while left <= right:
            # Calculate middle index
            mid = (left + right) // 2
            
            # Target found at mid
            if nums[mid] == target:
                return mid
            
            # Search in left half
            if nums[mid] > target:
                right = mid - 1
            # Search in right half
            else:
                left = mid + 1
        
        # Target not found, return insertion position
        return left