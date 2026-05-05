class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # Ok so i KNOW this is a dp problem. so in that case we need some sort of search based on a step
        # At each step we take a number and we can multiply it by any other number that other number cannot be multiplied
        # by it multipl etimes. we also can choose not to multiply by the given numbers I guess. So like starting at 1
        # we can go by 234 then from 234 we cant revisit 1 but we can go to each of the others. 

        # my challenge is how to model the n numbers we could then multiply by vs the multiply or dont multiply quesion

        # But then how would we get to every possible combination is my challenge
        # ok it also has to be continuous. So we cant jump around. That means at each step we can either multiply
        # or not multiply

        # So we want to start at every number then for each number we have two branches. one where we multiply and dont. 

        # start at 1. then we have two options 1*2 = 2 or stop. next we can go from 2 we can do 1*2*-3 or stop with 2
        # in this case stopping with 2 is greater so going from 1 this is the greatest value we can get. 
        
        # We can then start from 2. We know that from 2 we chose to stay instead of multiplyning by the next so here we can pull
        # from mem and stay again. Then starting at -3 we multiply by 4 and get -12 so we see that staying at -3 is best
        # we update mem. We can then go to 4. we cant go to the next but we know that staying at 4 is now the greatest. So
        # for each of our locations in the list we are able to figure out whether it is best to continue or stop. 
        res = max(nums)
        curMin, curMax = 1,1

        for num in nums:
            tmp = curMin * num
            curMin = min(num * curMin, num * curMax, num)
            curMax = max(tmp, num * curMax, num)
            
            res = max(res, curMin, curMax)



        return res



