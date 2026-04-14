class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        lkup = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        
        for p in s:
            print(p)
            if p in(lkup.keys()):
                stk.append(p)
            else:
                if len(stk) > 0: 
                    check = stk.pop()
                    if p != lkup[check]: return False
                else: return False
        
        if len(stk) ==0: return True
        return False

