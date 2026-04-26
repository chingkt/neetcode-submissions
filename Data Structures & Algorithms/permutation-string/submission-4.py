class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        hashMap = {}
        for char in s1:
            hashMap[char] = 1 if hashMap.get(char) == None else hashMap[char] + 1

        l, r = 0, 0
        while r < len(s2):
            tmpMap = hashMap.copy()
            if tmpMap.get(s2[l]) != None and tmpMap.get(s2[l]) != 0:
                while tmpMap.get(s2[r]) != None and tmpMap.get(s2[r]) != 0:
                    print(l, r)
                    if r - l + 1 == len(s1):
                        return True
                    tmpMap[s2[r]] -= 1
                    r += 1
                    if r >= len(s2):
                        return False
            l += 1
            r = l
            print(l, r)
        return False