class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        best = 0
        
        for n in nums:
            print(n) 
            if n-1 not in hs: 
                streak = 1
                while n+streak in hs:
                    streak +=1


                if streak > best: best = streak
        
        return best
            