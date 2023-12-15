# from typing import Counter
from collections import Counter


# 383. Ransom Note
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        st1, st2 = Counter(ransomNote), Counter(magazine)
        # intersection = st1 & st2
        # print(intersection)
        if st1 & st2 == st1:
            return True
        return False

    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        st1, st2 = Counter(ransomNote), Counter(magazine)
        for key in st1:
            if st1[key] > st2[key]:
                return False
        return True


if __name__ == '__main__':
    result = Solution()
    ransomNote = "abc"
    magazine = "aabbbcc"
    ans = result.canConstruct(ransomNote, magazine)
    print(ans)
