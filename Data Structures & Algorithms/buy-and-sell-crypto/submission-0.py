class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_min = math.inf
        current_max = 0
        for i in range(len(prices)):
            if prices[i] < current_min:
                current_min = prices[i]
            elif prices[i] - current_min > current_max:
                current_max = prices[i] - current_min

        return current_max