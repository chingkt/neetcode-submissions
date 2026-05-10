class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appearedNums = set()
        for num in nums:
            if num not in appearedNums:
                appearedNums.add(num)
            else:
                return True
        return False