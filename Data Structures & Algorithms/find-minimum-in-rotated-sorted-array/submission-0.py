class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1

        if nums[l]<nums[r]: 
            return nums[l]

        while l < r-1:
            
            m = l + (r-l)//2
            
            if nums[m] > nums[l]: l = m
            elif nums[m]< nums[l]: r = m
        
        return nums[r]