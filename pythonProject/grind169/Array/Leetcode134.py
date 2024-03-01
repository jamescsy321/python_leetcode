from typing import List


# 134. Gas Station
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1

        start = 0
        remain = 0

        for i in range(len(gas)):
            if gas[i] + remain < cost[i]:
                start = i + 1
                remain = 0
            else:
                remain += gas[i] - cost[i]

        return start


if __name__ == '__main__':
    result = Solution()
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    ans = result.canCompleteCircuit(gas, cost)
    print(ans)
