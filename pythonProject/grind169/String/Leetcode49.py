from collections import defaultdict
from typing import List


# 49. Group Anagrams
# medium
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solution = {}
        if len(strs) < 1:
            return list(strs)
        else:
            for i in range(len(strs)):
                reg = strs[i]
                regsort = "".join(sorted(reg))
                if regsort in solution:
                    solution[regsort].append(reg)
                else:
                    solution[regsort] = [reg]

            return list(solution.values())

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        # 建立一個字典，用於存儲同字母異序詞的映射,default值以一個list()方法產生
        anagram_map = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            # 將排序後的字串作為鍵，將原始單詞添加到相應的列表中
            anagram_map[sorted_word].append(word)
        # 返回字典中所有值的列表，這些值就是同字母異序詞的分組
        return list(anagram_map.values())


if __name__ == '__main__':
    result = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    ans = result.groupAnagrams2(strs)
    print(ans)
