class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        tmpArray = nums[0: k]
        print(len(nums))
        for i in range(len(nums) - k + 1):
            # one pass to init the window
            sortedTmpArray = sorted(tmpArray)
            res.append(sortedTmpArray[-1])
            if i < len(nums) - k:
                del tmpArray[0]
                tmpArray.append(nums[i+k])

        return res
                
            