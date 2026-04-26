class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = [(-math.inf, 0)] * 2001
        for num in nums:
            num += 1000
            count = counts[num][1]
            counts[num] = (num, count+1)

        counts.sort(key=lambda x: x[1], reverse=True)
        result_array = []
        for pair in counts[:k]:
            result_array.append(pair[0] - 1000)

        return result_array


        