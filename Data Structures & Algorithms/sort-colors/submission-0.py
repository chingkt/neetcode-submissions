class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 3

        for num in nums:
            counts[num] += 1
        
        for i in range(len(nums)):
            for j in range(len(counts)):
                if counts[j] > 0:
                    nums[i] = j
                    counts[j] -= 1
                    break