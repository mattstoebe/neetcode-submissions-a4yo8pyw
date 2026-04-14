class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        wordslist = []
        freqslist = []
        for word in strs:
            freqs = {}
            for char in word:
                if char in freqs:
                    freqs[char] += 1
                    
                else: freqs[char]=1
            
            if [freqs] not in freqslist:
                freqslist.append([freqs])
                wordslist.append([word])
            
            else: 
                index = freqslist.index([freqs])
                wordslist[index].append(word)
            
        return wordslist
                
            
                
