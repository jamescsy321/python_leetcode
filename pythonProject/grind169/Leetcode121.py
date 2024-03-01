from typing import List


# 121. Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit


if __name__ == '__main__':
    result = Solution()

    prices = [7, 1, 5, 3, 6, 4]
    ans = result.maxProfit(prices)
    print(ans)
