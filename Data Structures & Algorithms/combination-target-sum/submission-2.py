class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # So here im thinking we start at element 0. Then we have two branches. First we
        # Can add the number to ourselves. Second we can add the next number
        n = len(nums)
        res, sol = [], []

        def backtrack(i):

            # theres a few cases here. 
            # First we can go over. That means our current branch is useless
            # Second we can hit the end that means curren tneeds to be the value
            # finally we can find the nmber. this means we cant keep iterating. We know
            # all numbers are positive so once we get over target, we dont keep iterating
            
            if i == n: # when we hit the end we check
                if sum(sol) == target:
                    res.append(sol[:])
                    return
                else:
                    return
            
            if sum(sol) == target:
                res.append(sol[:])
                return # We dont need to continue down this branch

            if sum(sol) > target:
                return
            
            # So here we skip this target
            backtrack(i+1)

            # here we use the target
            sol.append(nums[i])
            backtrack(i)
            sol.pop()

        backtrack(0)
        return res

            
