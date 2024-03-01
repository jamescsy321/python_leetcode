# 278. First Bad Version
def isBadVersion(mid):
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n

        while low <= high:
            mid = (high + low) // 2
            if isBadVersion(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low


if __name__ == '__main__':
    result = Solution()
    n = 5
    bad = 4
    ans = result.firstBadVersion(n)
