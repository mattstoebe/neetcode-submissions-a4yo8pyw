class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        


        ln = len(s)
        if ln <= 1: return ln

        lst_vwd = {
            s[0]:0
        }


        l,r = 0,1
        max_length = 0
        
        while r < ln:
            print(l,r, s[l], s[r])
            lst_vw_r = lst_vwd.get(s[r])
            if lst_vw_r != None and  lst_vw_r >=l:
                print("string ending")
                lst_vwd[s[r]] = r
       
                
                length = r-l
                if length > max_length: max_length = length
                print()
                l = lst_vw_r+1
                r +=1

            else:
                lst_vwd[s[r]] = r
                r+=1
                
        final_length = r - l
        if final_length > max_length: return final_length
        return max_length


