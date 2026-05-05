class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Ok so we could say the repeated problem is checking if a remaining chunk is composable of certain words
        # So say we take word 1 and it matches the first n characters then we have to know if characters n:end are
        # completeable. So the mem would be index:True/False

        # so we would kick off a sub problem for each possible subcase starting from the given index

        mem = {}
        
        def dp(idx):
            
            # Here we got to the end of the string. if we get to teh end of the string that means this case is valid
            if idx == len(s):
                return True

            if mem.get(idx, None) != None:
                return mem[idx]

            # Otherwise, we need to see if one of our words can fill the next n characters in the string
            for word in wordDict:
                end_idx = idx + len(word)
                if s[idx:end_idx] == word:
                    out = dp(end_idx)
                    if out == True: 
                        mem[idx] = True
                        return True
            
            # we looped through all words and found that we cannot complete from there so we mark it as false
            mem[idx] = False
            return False

        return dp(0)