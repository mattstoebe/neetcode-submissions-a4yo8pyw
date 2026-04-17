class Solution:
    mem = {}
    def climbStairs(self, n: int ) -> int:
        # So at each step we can either take a step forward or take two steps forward. 
        # this reduces the number of remaining steps by step size
        
        # So i ran out of time but what I need is when I get to 1
        if self.mem.get(n): return self.mem[n]

        if n == 0:
            return 1
        if n < 0: 
            return 0

        
        self.mem[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.mem[n]
