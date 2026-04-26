class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        left, right = 0,0
        hashSet = set()
        res = 0
        while right < len(s):
            if s[right] in hashSet:
                print("duplicate:", s[right])
                while s[left] != s[right]:
                    hashSet.remove(s[left])
                    left += 1
                left += 1
            else:
                hashSet.add(s[right])
            if right - left + 1 > res:
                res = right - left + 1
            right += 1
            print(left, right, res)
        return res
