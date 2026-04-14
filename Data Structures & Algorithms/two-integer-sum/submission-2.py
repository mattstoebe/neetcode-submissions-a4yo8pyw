class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        numdict = {} # I need the number and the index
        for i, num in enumerate(nums):
            rem = target - num # Remainder needed
            
            # check if the remainder is in the dict. If it is get out the index
            if rem in numdict: return [numdict[rem], i]
            
            # otherwise add the index to the numdict
            numdict[num] = i
            