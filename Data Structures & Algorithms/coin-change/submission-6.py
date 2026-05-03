class Solution:
    best = float('inf')
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        #So you can always take the same coin again or 
        # move to the next coin        
        def dfs(idx:int, running:int, used: float) -> int:
            # base condition is basically running over the end of the string

            if idx >= len(coins):
                return
        
            if running > amount:
                return

            if running == amount and (self.best == None or used < self.best):
                self.best = used
                return
            
            if used > self.best:
                return

            # dont take
            dfs(idx +1, running, used)

            # take
            dfs(idx, running + coins[idx], used +1)

            

        dfs(0,0,0)
        if self.best == float('inf'): return -1
        return int(self.best)
 

