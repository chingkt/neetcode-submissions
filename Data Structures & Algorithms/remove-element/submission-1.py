class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for ind, num in enumerate(nums):
            if num == val:
                nums[ind] = 51
            else:
                k += 1
        
        nums.sort()
        return k
        