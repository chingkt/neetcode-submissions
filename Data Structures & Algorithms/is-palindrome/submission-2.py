class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            while s[i].isalnum() != True:
                i += 1
                if i > len(s) - 1:
                    break
            while s[j].isalnum() != True:
                j -= 1
                if j < 0:
                    break
            if i > j or i > len(s) - 1 or j < 0:
                break

            if s[i].lower() != s[j].lower():
                print(i, j, s[i], s[j])
                return False
            else:
                i += 1
                j -= 1
        return True