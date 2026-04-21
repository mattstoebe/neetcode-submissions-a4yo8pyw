class Solution:
    def numDecodings(self, s: str) -> int:
        # So we first need to build the encode decode map it seems
        # Then we loop through all possible decoding groupings and check
        # if all groups are valid.

        # The repeated work seems to be the ramifications of the first split
        # Like each split can have a certain number of digits that has implications
        # on how the next can be split up

        # The other probelm is there are like infinite branches. so how do you break it into sub problems
        # Maybe we start character by caharcter and then we aggregate different ways 

        # ok i figured out how to generate the tree. We need to do the split and then pass the split and 
        # a pointer down to the next level. we always iterate the pointer by 1 but and then decide to split o rnot split at that index
        
        # So then we are taking the string at lp and dtermining if the substring it creates is a valid 
        # thing to decode. but this should only be done at the bottom. we can then bring it back up and say 
        def dp(p):

            if p in mem:
                return mem[p]
            
            if p >= len(s):
                return 1

            cnt = 0

            if s[p] != "0":
                cnt += dp(p + 1)

                if p + 1 < len(s) and int(s[p:p+2]) <= 26:
                    cnt += dp(p + 2)
            mem[p] = cnt
            return cnt

        mem = {}
        return(dp(0))




