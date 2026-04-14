class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1

        #our goal is to reduce this to standard binary search. 
        # first lets just try to find the split. then we can figure out how to search

        while l<r:

            m = l + (r-l) //2
            if nums[m] == target: return m

            # check which side is sorted
            if nums[l] <= nums[m]:
                print("left is sorted")
                if nums[l] <= target <= nums[m]:
                    print("target on the left half")
                    r = m-1
                
                else: 
                    print("target still in unsorted region")
                    l = m+1
            else:
                print("right is sorted")
                if nums[m] <= target <= nums[r]:
                    print("target is on the right half")
                    l = m+1
                else:
                    print("target in unsorted region")
                    r = m-1

            
        if nums[l] == target: return l
        return -1                