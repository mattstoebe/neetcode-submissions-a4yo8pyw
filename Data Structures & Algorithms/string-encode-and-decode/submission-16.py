class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # Format: [length] + [#] + [string]
            # Example: ["", "abc"] -> "0#3#abc"
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        
        while i < len(s):
            j = i
            # Find the separator to know where the length ends
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            # The string starts right after the '#'
            start = j + 1
            end = start + length
            res.append(s[start:end])
            
            # Move the pointer to the start of the next length prefix
            i = end
            
        return res