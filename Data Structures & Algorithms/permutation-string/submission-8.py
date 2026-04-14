class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        tgt_ln = len(s1)
        tgt_map = {}
        for l in s1:
            tgt_map[l] = tgt_map.get(l,0) + 1
        
        cw = {}
        l,r = 0, 0

        for r in range(len(s2)):
            cw[s2[r]] = cw.get(s2[r],0)+1
            if cw == tgt_map: return True
            print(cw, tgt_map)
            if r - l+1 == len(s1):
                cw[s2[l]] = cw.get(s2[l],0)-1
                if cw[s2[l]] == 0: del cw[s2[l]]
                l+=1
            
            r+=1

        return False
