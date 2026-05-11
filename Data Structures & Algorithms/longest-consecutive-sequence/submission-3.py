class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        integerSet = set()
        for num in nums:
            integerSet.add(num)
        
        maxLength = 0

        for num in nums:
            currentLength = 1
            while num + 1 in integerSet:
                currentLength += 1
                num += 1
            if currentLength > maxLength:
                maxLength = currentLength
        return maxLength
