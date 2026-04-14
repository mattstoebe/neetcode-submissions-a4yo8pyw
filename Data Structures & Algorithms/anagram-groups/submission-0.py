class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(s, t):
            freq1 = {}
            freq2 = {}
            if len(s) != len(t): return False
            # check each letter appears at the same frequency
            
            for i in range(0, len(s)):
                if s[i] in freq1: freq1[s[i]] +=1
                else: freq1[s[i]] = 1  

                if t[i] in freq2: freq2[t[i]] +=1
                else: freq2[t[i]] = 1
            
            return freq1 == freq2


        all_grams = [[strs[0]]]


        for word in strs[1:]:
            cnt = 0
            for gram in all_grams:
                if isAnagram(s = gram[0], t=word):
                    gram.append(word)
                    cnt += 1
                    break
            if cnt == 0:
                all_grams.append([word])

        return(all_grams)



    