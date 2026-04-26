class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        currentSubstring = ""
        maxLength = 0
        hashmap = {}
        left, right = 0, 0
        while right < len(s):
            currentSubstring += s[right]
            if hashmap.get(s[right]) == None:
                hashmap[s[right]] = 1
            else:
                hashmap[s[right]] += 1
            right += 1

            requiredNumOfSameElem = len(currentSubstring) - k
            hasRequiredNumOfSameElem = False
            for _, v in hashmap.items():
                if v >= requiredNumOfSameElem:
                    hasRequiredNumOfSameElem = True
                    if len(currentSubstring) > maxLength:
                        maxLength = len(currentSubstring)
                    break
            if not hasRequiredNumOfSameElem:
                if len(currentSubstring) - 1 > maxLength:
                    maxLength = len(currentSubstring) - 1
                left += 1
                hashmap[currentSubstring[0]] -= 1
                currentSubstring = currentSubstring[1:]
        return maxLength
