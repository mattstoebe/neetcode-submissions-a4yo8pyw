class Solution:
    def countSubstrings(self, s: str) -> int:
        # This should be the same as my last question solved jsut tweaking the logic

        def isPalindrome(l,r):
            key = (l,r)
            if key in mem:
                return mem[key]

            if l >= r:
                # Base case we reached the end
                return True

            # This is not a palindrome so we return False
            if s[l] != s[r]:
                return False

            sub_passes = isPalindrome(l+1, r-1)

            mem[key] = sub_passes
            return sub_passes

        cnt = 0
        mem = {}

        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1]
                if isPalindrome(i,j):
                    cnt +=1

        return cnt