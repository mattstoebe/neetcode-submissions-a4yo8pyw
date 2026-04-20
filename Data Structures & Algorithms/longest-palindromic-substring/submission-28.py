class Solution:
    def longestPalindrome(self, s: str) -> str:
        # We need to run is palindrome but multiple times
        # But because its DP we can figure that we need to store some data for later

        # So to find a palindrome we have a left and right pointer that are equal then we need to 
        # iterate in until they are at the same point. This then tells us we have a palindrome

        # We could on our first scan find all places where the letters are and then check each possible 
        # Palindrome, Like we know therea re two as so we check is palindrome aa and then we know there
        # are two bs so we check there. 

        # LEts start with brute force:

        def isPalindrome(l,r):
            key = (l,r)
            if key in mem:
                return mem[key]
            if l >=r:
                return True
            
            if s[l] != s[r]:
                mem[key] = False
                return False

            below = isPalindrome(l+1, r-1)

            mem[key] = (True and below)
            return True and below


        # So we can check is palindrome but we dont want to check for the same string multiple times
        # We also dont want to check for strings that are smaller than our curent best

        best = 0
        longest = ""
        mem = {}

        if len(s) == 1:
            return s

        for i in range(len(s)):
            for j in range(i,len(s)):
                sub = s[i:j+1]
                sub_len = j-i +1
                sub_passes = isPalindrome(i,j)
                if sub_passes and sub_len > best:
                    best = sub_len
                    longest = sub

        return longest

