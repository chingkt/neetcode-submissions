class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLength = 201
        prefix = ""
        for s in strs:
            if len(s) < minLength:
                minLength = len(s)
        
        for i in range(minLength):
            prefixOfFirstString = strs[0][i]
            print(prefixOfFirstString)
            for s in strs:
                if s[i] != prefixOfFirstString:
                    return prefix
            prefix += prefixOfFirstString
        return prefix