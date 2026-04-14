class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # I know that in these problems it is common to maitain a frequency map and check equality
        # We could create two frequency maps and iterate our two pointers from left to right
        # They would move together until it finds a letter that is in our target string, 
        #then the other pointer would iterate forward checking for all other letters n our target string. 
        # We would then store the next "starting" letter and jump L to there if R ddidnt find the substring
        # The problem here is that it is worst case n2 time 

        # Alternativey I could search for the end instead of the start. If I do one scan
        # with rright pointer an di record the positions of all the letters I care about and make sure I 
        # have everything I need, I could then iterate my left pointer removing from what we have until
        # we have exactly what we need, no more no o less. Then one meore step to leave that found substring
        # and we can strat moving the right pointer again until we find another region where we have it all.
        def check_maps_complete(target_map: dict, freq_map: dict) -> bool:
            fail = 0
            for key, value in target_map.items():
                if freq_map.get(key,0) <  target_map.get(key,0):
                    fail +=1

            return fail == 0
        
        l, r = 0, 0
        
        target_map = {}
        freq_map = {}
        minlength = len(s)
        minstring = ""

        for letter in t:
            target_map[letter] = target_map.get(letter,0) + 1


        while r < len(s):
            print("spreading", l, s[l], r, s[r])
            if target_map.get(s[r],0) > 0:
                
                freq_map[s[r]] = freq_map.get(s[r],0) + 1
                complete = check_maps_complete(target_map, freq_map)

                while complete:
                    print("tightening", l, s[l], r, s[r])
                    candidate_string = s[l:r+1]
                    if len(candidate_string) <= minlength:
                        minstring = candidate_string
                        minlength = len(candidate_string)
                        print("new best", minstring)

                    if target_map.get(s[l],0) > 0:
                        freq_map[s[l]] = freq_map.get(s[l],0) - 1
                    complete = check_maps_complete(target_map, freq_map)
                    
                    l+=1

            r+=1

        return minstring





            





