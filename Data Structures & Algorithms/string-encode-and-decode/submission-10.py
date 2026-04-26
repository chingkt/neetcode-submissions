class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            num = len(s)
            res += str(num) + "%" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "%":
                j += 1
            length = int(s[i:j])
            tmp_str = s[j+1:j+1+length]
            res.append(tmp_str)
            i = j + length + 1
        return res

