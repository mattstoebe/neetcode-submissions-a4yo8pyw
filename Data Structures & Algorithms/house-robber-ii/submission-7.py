class Solution:
    def rob(self, nums: List[int]) -> int:
        # I feel that this should be the same but iwth an udpate on the base conditions
        # Ok the difference tho is that we cannont like figure out all info from just rob1 rob2
        # Because we need to know where this branch started. 
        # Basically we need. way to make the first rob and the last rob communicate. If a branch
        # starts with robbing house 0 then we cannot go rob the last house. so the behavior on the 
        # Left and right side of the tree needs to be different

        # This also means that the memoized "best" amount is different on each side of the tree. 
        # Thi smakes me think we pass two items both into memo and into dp which is True/False for first house
        # and then the iteration. 

        mem = {} # (int, bool) int
        houses = len(nums)

        def dp(n:int, first_robbed:bool):
            
            key = (n, first_robbed)
            if key in mem:
                return mem[key]

            # handle case when first house was robbed. This needs to end early
            if n == houses-1 and first_robbed:
                return 0

        
            # In the case where the first house was not robbed, we also return 0
            if n >= houses:
                return 0
            

            # Here we dont rob current house and we iterate to the next
            rob1 = dp(n+1, first_robbed)
            # Here we rob current house and then skip the next
            rob2 = nums[n] + dp(n+2, first_robbed)

            best = max(rob1, rob2)

            mem[key] = best
            return best

        
        rob1 = nums[0] + dp(2,True)
        skip1 = dp(1,False)
        
        return max(rob1,skip1)
        
        