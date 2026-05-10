class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for idx, num in enumerate(nums):
            if not hashMap.get(num):
                hashMap[num] = {"idx": [idx], "num": num}
            else:
                hashMap[num]["idx"].append(idx)

        for idx, num in enumerate(nums):
            anotherNum = target - num
            if hashMap.get(anotherNum):
                if anotherNum != num:
                    return [min(idx, hashMap[anotherNum]["idx"][0]), max(idx, hashMap[anotherNum]["idx"][0])]
                elif hashMap[anotherNum]["idx"][0] != idx:
                    return hashMap[anotherNum]["idx"]

