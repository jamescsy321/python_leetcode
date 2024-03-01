import math
from typing import List


# 438. Find All Anagrams in a String
# sliding window
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        start = 0
        matched = 0
        lookup = {}
        result_list = []

        for char in p:
            lookup[char] = lookup.get(char, 0) + 1

        for end in range(len(s)):
            right = s[end]
            if right in lookup:
                lookup[right] -= 1

                if lookup[right] == 0:
                    matched += 1

            if matched == len(lookup):
                result_list.append(start)

            if end >= len(p) - 1:
                left = s[start]
                if left in lookup:
                    if lookup[left] == 0:
                        matched -= 1
                    lookup[left] += 1
                start += 1

        return result_list


if __name__ == '__main__':
    result = Solution()
    s = "cbaebabacd"
    p = "abc"
    ans = result.findAnagrams(s, p)
    print(ans)
