class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left poitner sits at current max-minimum.
        # We iterate right pointer. If right pointer hits a new max we update total value
        # if right pointer hits new minium we update left pointer to = right pointer

        l = 0
        r = 1

        max_profit = 0
        ln = len(prices)
        if ln == 1: return max_profit

        while r < ln:
            print(prices[l], prices[r])
            gap = prices[r] - prices[l]
            print(prices[l], prices[r])

            if gap > max_profit:
                max_profit = gap
            
            if prices[r] < prices[l]:
                l = r

            r+=1
        
        return max_profit