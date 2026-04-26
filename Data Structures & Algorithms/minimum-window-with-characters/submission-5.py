class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        l,r = 0,0
        res = ""

        sCounts = {}
        while r < len(s):
            valid = False
            if s[r] not in t:
                sCounts[s[r]] = 1 if sCounts.get(s[r]) == None else sCounts[s[r]] + 1
                r += 1
                print("if s[r] not in t", l ,r, sCounts)
                continue
            while not valid:
                if r >= len(s):
                    break
                sCounts[s[r]] = 1 if sCounts.get(s[r]) == None else sCounts[s[r]] + 1
                r += 1
                valid = self.isValid(sCounts.copy(), t)
                print("while not valid", l ,r, sCounts)
            if not valid:
                continue
            while valid:
                sCounts[s[l]] -= 1
                l += 1
                valid = self.isValid(sCounts.copy(), t)
                print("while valid", l ,r, sCounts)


            res = s[l-1:r] if len(s[l-1:r]) < len(res) or res == "" else res
            print("res assignemnt", res, l, r)
        return res

    def isValid(self, sCounts: Dict, t: str) -> bool:
        for c in t:
            if sCounts.get(c) == None or sCounts.get(c) <= 0:
                return False
            sCounts[c] -= 1
        return True