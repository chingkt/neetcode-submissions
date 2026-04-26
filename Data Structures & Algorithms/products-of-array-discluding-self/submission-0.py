class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodPrefixes = [1] * len(nums)
        prodPostfixes = [1] * len(nums)
        res = [1] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                prodPrefixes[i] = nums[i]
            else:
                prodPrefixes[i] = prodPrefixes[i-1] * nums[i]
        
        for j in range(len(nums)-1, -1, -1):
            if j == len(nums)-1:
                prodPostfixes[j] = nums[j]
            else:
                prodPostfixes[j] = prodPostfixes[j+1] * nums[j]
        
        for i in range(len(nums)):
            if i == 0:
                res[i] = prodPostfixes[i+1]
            elif i == len(nums) - 1:
                res[i] = prodPrefixes[i-1]
            else:
                res[i] = prodPostfixes[i+1] * prodPrefixes[i-1]
        return res