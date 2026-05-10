class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = 1 if not counts.get(num) else counts[num] + 1
        sortedArray = [k for k,_ in sorted(counts.items(), key= lambda item: item[1], reverse=True)]
        return sortedArray[:k]