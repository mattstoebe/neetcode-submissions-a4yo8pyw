class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # naive
        # we can access values in an array in O(1) time. 
        #so if for each element of the array we can access all other elements in a while loop
        ln = len(nums)
        
        # Brute force
        out = [1 for _ in range(ln)]
        print(out)
        for i, num1 in enumerate(nums): 
            for j, num2 in enumerate(nums): 
                if i == j:
                    pass
                else: out[i] *= num2

        return out