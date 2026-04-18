class Solution:
    def rob(self, nums: List[int]) -> int:
        # So tis like when we rob H7, we only have two options. Once we get the best amount of money we could have at 
        # house 7 we never need to explore that way again. From y you can only get n more dollars. save that in memo

        mem = {}
        houses = len(nums)
        
        def dp(n):
                        
            # base case we have no more houses to rob
            if n >= houses:
                return 0
            
            if n in mem:
                return mem[n]
            print(n, nums[n])
            
            # There are two things. Firstw e need to get the sum along the branch
            # and then second we need to get the best branch
            left = dp(n+2)
            right = dp(n+3)
            best = max(left, right) + nums[n]
            mem[n] = best
            
            return best

        return max(dp(0), dp(1))