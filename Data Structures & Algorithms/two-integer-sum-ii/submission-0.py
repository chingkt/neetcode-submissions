class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            anotherNumber = target - numbers[right]
            if numbers[left] == anotherNumber:
                break
            if numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return [left+1, right+1]