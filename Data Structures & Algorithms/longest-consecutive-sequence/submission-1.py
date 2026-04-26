class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        existingNumbers = set()

        for num in nums:
            existingNumbers.add(num)

        max_length = 0
        current_length = 0
        for num in nums:
            if num - 1 not in existingNumbers:
                current_length = 0
                curr = num
                while True:
                    if curr in existingNumbers:
                        current_length += 1
                        curr += 1
                        if current_length > max_length:
                            max_length = current_length
                    else:
                        break
        return max_length


