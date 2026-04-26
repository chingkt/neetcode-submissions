class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            for char in s:
                res += str(ord(char)) + "%"
            res += "!"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        tmp_char = ""
        tmp_str = ""
        for char in s:
            match char:
                case "!":
                    res.append(tmp_str)
                    tmp_str = ""
                case "%":
                    tmp_str += chr(int(tmp_char))
                    tmp_char = ""
                case _:
                    tmp_char += char
        return res
