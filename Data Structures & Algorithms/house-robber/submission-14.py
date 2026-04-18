class Solution:
    def rob(self, nums: List[int]) -> int:
        # Ive already solved with a bottom up tree but now want to solve it going left
        # To right. 

        # So at each step, we can either rob the house we are at or the next one. but there
        # Is some weird situation with how we move our pointers. 

        # So i remember a little bit of how this looks
        rob1, rob2 = 0,0
        
        # At each place we only need to track the max of robbing the last one vs two before

        # so we want to loop through the houses we can rob and then look at the decisions we have
        for n in nums:
            # Here we can make a choice to rob house at n or the next one. but we cant do both
            # So we have some running total and then we see which house it is better to rob

            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
            
        return max(rob1, rob2)