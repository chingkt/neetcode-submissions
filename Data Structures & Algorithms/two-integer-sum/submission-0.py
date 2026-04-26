class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for ind, num in enumerate(nums):
            anotherNum = target - num
            indAnotherNum = hashMap.get(anotherNum)
            if indAnotherNum != None:
                if ind < indAnotherNum:
                    return [ind, indAnotherNum]
                else:
                    return [indAnotherNum, ind]
            else:
                hashMap[num] = ind