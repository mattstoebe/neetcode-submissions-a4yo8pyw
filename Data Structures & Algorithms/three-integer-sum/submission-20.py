class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        out = []
        
        # I think i can controll duplicates by sorting it instead of checking a visited 
        nums.sort()
        i = 0
        
        # outer loop
        while i < len(nums):
            l = i+1
            r = len(nums)-1

            while l<r:
                tot = nums[l] + nums[r] + nums[i]

                if tot < 0: l+=1
                if tot >0: r-=1

                if tot == 0:
                    out.append([nums[i],nums[l], nums[r]])
                    l+=1
                    r-=1
                    # skip over internal loop duplicates
                    while l < len(nums) and nums[l] == nums[l-1]:
                        l+=1
                    while r > l and nums[r] == nums[r+1]:
                        r-=1
            
            #Iterate to next element in nums
            i+=1
            # If next element is same as last, skip over it
            while i < len(nums) and nums[i] == nums[i-1]:
                i+=1


        return out