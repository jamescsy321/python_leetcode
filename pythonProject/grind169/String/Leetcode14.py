from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    ans = ""
    str_list = sorted(strs)
    first = str_list[0]
    last = str_list[-1]
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return ans
        ans += first[i]
    return ans


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    result = longestCommonPrefix(strs)
    print(result)
