class Solution:
    def sortSubarray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        if n >= 2:
            left = self.sortSubarray(nums[:math.ceil(n/2)])
            right = self.sortSubarray(nums[math.ceil(n/2):])
            tempArray = []
            i = j = 0
            while len(tempArray) != len(left) + len(right):
                if j == len(right):
                    tempArray += left[i:]
                    return tempArray
                elif i == len(left):
                    tempArray += right[j:]
                    return tempArray
                if left[i] > right[j]:
                    tempArray.append(right[j])
                    j += 1
                else:
                    tempArray.append(left[i])
                    i += 1
            return tempArray
        return nums


    def sortArray(self, nums: List[int]) -> List[int]:
        return self.sortSubarray(nums)