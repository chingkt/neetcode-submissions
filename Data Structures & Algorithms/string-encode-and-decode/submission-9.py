class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            num = len(s)
            res += str(num) + "%" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        tmp_length = 0
        tmp_length_str = ""
        length_read = False
        tmp_str = ""
        res = []
        if s == "":
            return res
        for char in s:
            if not length_read:
                if char == "%":
                    length_read = True
                    tmp_length = int(tmp_length_str)
                    tmp_length_str = ""
                else:
                    tmp_length_str += char
            elif tmp_length == len(tmp_str):
                res.append(tmp_str)
                tmp_str = ""
                length_read = False
                tmp_length_str += char
            else:
                tmp_str += char
        res.append(tmp_str)

        return res

