class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # To create a subsequence, we can delete or keep a given number in the sequence. 
        # I guess we can iterate on this until we are down to a single number. the repeated
        # work is then checking if a given number is I guess greater than the number returned from below it?
        # Or i guess we actually for each number want to pass the biggest growing sequence we can generate from 
        # it. 

        # So say we keep 9 then the next number can be any number after 9. so we grab them all and loop through
        # but none are valid so we dont recurse. 

        # Then we grab 1. All the following numbers are valid so we recurse. If we hop onto the 4 branch then only 7 is valid
        # so we return 7 > 4 > 1. but at each level we are able to figure out what the max from that number is 
        # so like the max from 4 is 1 because 4 7 but from 1 we could go 147 1237 137 etc.. so we know the max from 1 is 4

        mem = {}

        def dp(idx):
            
            # Figure out base case
            

            # mem case
            if idx in mem:
                return mem[idx]

            best = 1
            for i, num in enumerate(nums[idx+1:]):
                true_index = i + idx+1
                if num > nums[idx]: # if a flloiwng number is greater we recurse
                    best = max(best, 1+dp(true_index))

            mem[idx] = best

            return best


        out = 0
        for i in range(0,len(nums)):
            out = max(out, dp(i))

        return out





