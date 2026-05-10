class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}
        for c in s:
            countS[c] = 1 if not countS.get(c) else countS[c] + 1
        for c in t:
            countT[c] = 1 if not countT.get(c) else countT[c] + 1
        
        return countS == countT

        