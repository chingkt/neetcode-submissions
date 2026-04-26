class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        counts = {}
        for num in nums:
            if counts.get(num) != None:
                counts[num] += 1
            else:
                counts[num] = 1
        for key in counts.keys():
            freq[counts[key]].append(key)
            print(counts[key], key, freq)
        res = []
        i = len(freq) - 1
        j = 0
        while j < k:
            for elem in freq[i]:
                res.append(elem)
                j += 1
            i -= 1
        return res