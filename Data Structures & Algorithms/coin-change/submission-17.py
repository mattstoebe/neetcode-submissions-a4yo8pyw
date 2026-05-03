class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        mem = {}
        def dp(remaining:int):

            # Memo
            if remaining in mem:
                return mem[remaining]
            # Overshoot
            if remaining < 0:
                return amount+1
            if remaining == 0:
                return 0


            # Look at each coin we could jump to. I can also try a take vs dont take framing 
            subbest = amount + 1
            for coin in coins:
                subbest = min(subbest, 1+ dp(remaining - coin))


            mem[remaining] = subbest
            return subbest

            
        out = dp(amount)
        return out if out <= amount else -1
