from typing import List


# 322. Coin Change
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [-1] * amount  # init

        for x in range(amount):
            if dp[x] < 0:
                continue
            for c in coins:
                if x + c > amount:  # 相加超過所要求的和就跳過
                    continue
                if dp[x + c] < 0 or dp[x + c] > dp[x] + 1:
                    dp[x + c] = dp[x] + 1
        return dp[amount]


if __name__ == '__main__':
    result = Solution()
    coins = [1, 2, 5]
    amount = 11
    ans = result.coinChange(coins, amount)
    print(ans)
