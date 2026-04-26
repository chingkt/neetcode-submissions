class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L = 0
        R = len(nums) - 1
        i = 0
        while i <= R:
            if nums[i] == 0:
                nums[i] = nums[L]
                nums[L] = 0
                i += 1
                L += 1
            elif nums[i] == 2:
                nums[i] = nums[R]
                nums[R] = 2
                R -= 1
            else:
                i += 1
            print(L,i,R)

