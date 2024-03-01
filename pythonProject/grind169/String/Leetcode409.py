# 409. Longest Palindrome
#  easy
import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        map_dict = {}

        for i in s:
            if i in map_dict.keys():
                map_dict[i] += 1
            else:
                map_dict[i] = 1
        result = 0
        mark = 0

        for j in map_dict.keys():
            if map_dict[j] % 2 == 1:
                mark += 1
            result += map_dict[j]

        result = result * 2 + 1 if mark > 0 else result * 2
        return result if result > 0 else (1 if mark > 0 else 0)

    def longestPalindrome2(self, s: str) -> int:
        odds = sum(v & 1 for v in collections.Counter(s).values())
        return len(s) - odds + bool(odds)

    def longestPalindrom3(self, s: str) -> int:
        # 用set計算有幾個奇數
        hash = set()
        for c in s:
            if c not in hash:
                hash.add(c)
            else:
                hash.remove(c)
        # len(hash) is the number of the odd letters
        test = len(s) - len(hash) + 1 if len(hash) > 0 else len(s)

        return len(s) - len(hash) + 1 if len(hash) > 0 else len(s)


if __name__ == '__main__':
    result = Solution()
    s = "abccccdd"
    ans = result.longestPalindrom3(s)
    print(ans)
