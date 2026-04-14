class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ln = len(s)
        # Basically, While the gap - max frequency is less than k we bump the right pointer
        # When it = k, we iterate left pointer updating the frequencies and the running max frequency
        # until we get to a point where we can start ierating the right pointer again.  
        freqs = {}
        max_freqs = 1
        max_gap = 0
        l = 0

        for r in range(ln):
            
            freqs[s[r]] = freqs.get(s[r],0) + 1
            max_freqs = max(max_freqs, freqs[s[r]])  
        
            while ((r-l+1) - max_freqs) > k:
                freqs[s[l]] -= 1
                l+=1

            max_gap = max(max_gap, r-l+1)

        
        return max_gap


            
            




