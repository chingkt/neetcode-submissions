class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i, j, n = 0, 1, len(nums)
        hashMap = {}
        triplets = []
        for idx, num in enumerate(nums):
            if hashMap.get(num) != None:
                hashMap[num] = hashMap.get(num) + [idx]
            hashMap[num] = [idx]

        for i in range(n - 1):
            for j in range(n - 1):
                if i == j:
                    break
                targetNum = - nums[i] - nums[j]
                targetIdxes = hashMap.get(targetNum)
                if targetIdxes != None:
                    for targetIdx in targetIdxes:
                        if targetIdx != None and targetIdx != i and targetIdx != j:
                            resultHash = {}
                            if resultHash.get(targetNum) != None:
                                resultHash[targetNum] += 1
                            else:
                                resultHash[targetNum] = 1
                            if resultHash.get(nums[i]) != None:
                                resultHash[nums[i]] += 1
                            else:
                                resultHash[nums[i]] = 1   
                            if resultHash.get(nums[j]) != None:
                                resultHash[nums[j]] += 1
                            else:
                                resultHash[nums[j]] = 1                      
                            if resultHash not in triplets:
                                triplets.append(resultHash)

        resList = []
        for s in triplets:
            res = []
            for k in s.keys():
                for _ in range(s[k]):
                    res.append(k)
            resList.append(res)

        return resList
