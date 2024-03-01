# 70. Climbing Stairs
class Solution:
    def climbStairs(self, n: int) -> int:
        prev, current = 0, 1
        for i in range(n):
            prev, current = current, prev + current
        return current


if __name__ == '__main__':
    result = Solution()
    n = 5
    ans = result.climbStairs(n)
    print(ans)
