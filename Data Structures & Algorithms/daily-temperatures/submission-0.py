class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))]

        stack = []
        for idx, temp in enumerate(temperatures):
            while len(stack) > 0 and stack[-1]["temp"] < temp:
                elem = stack.pop()
                res[elem["idx"]] = idx - elem["idx"]
            stack.append({"temp": temp, "idx": idx})
        return res

