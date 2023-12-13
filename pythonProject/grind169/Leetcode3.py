# 3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window 解法
        left = 0
        max_length = 0
        index_lookup = {}
        for right in range(len(s)):
            # 如果right字元曾在index_lookup的dict中，代表字元曾出現過，所以要更新left位置
            if s[right] in index_lookup:
                left = max(left, index_lookup[s[right]] + 1)

            index_lookup[s[right]] = right
            # 每次迴圈都計算目前找到的子字串長度，＋1是因為index從0起算
            max_length = max(max_length, right - left + 1)
        return max_length

    def lengthOfLongestSubstring2(self, s: str) -> int:
        seen = {}
        left = 0
        max_length = 0
        for r in range(len(s)):
            """
            If s[r] not in seen, we can keep increasing the window size by moving right pointer
            """
            if s[r] not in seen:
                max_length = max(max_length, r - left + 1)
            else:
                """
                            There are two cases if s[r] in seen:
                            case1: s[r] is inside the current window, we need to change the window by moving left pointer to seen[s[r]] + 1.
                            case2: s[r] is not inside the current window, we can keep increase the window
                """
                # 如果該字元的索引小於 left，表示該字元不在當前的子字串中，可以增加窗口大小，更新 max_length。
                # 如果該字元的索引大於或等於 left，則需要調整窗口大小，將 left更新為該字元上一次出現的位置的下一個索引。
                # 當在字典 seen 中發現目前的字元 s[r] 已經在之前出現過時，程式檢查了兩種情況：
                # seen[s[r]] < l：這表示目前的字元 s[r] 上一次出現的位置在當前窗口的左側，也就是它不在目前的窗口內。這時可以將窗口右移
                # ，增加窗口大小，因為字元 s[r] 是一個新的、不重複的字元，所以可以更新 output 的值。
                # seen[s[r]] >= l：這表示目前的字元 s[r] 上一次出現的位置在或超過了當前窗口的左邊界。
                # 這種情況下，需要調整窗口的起始位置 left，使其指向上一次出現的位置的下一個索引，以確保窗口內的所有元素都是不重複的。
                # 這樣做可以維持一個有效的窗口範圍，確保在窗口內的字元都是不重複的，同時透過移動窗口來找到最長的不重複字元子字串。
                if seen[s[r]] < left:
                    max_length = max(max_length, r - left + 1)
                else:
                    #  這個動作是為了調整窗口的起始位置 left，確保窗口內的元素都是不重複的。
                    left = seen[s[r]] + 1
            seen[s[r]] = r

        return max_length


if __name__ == '__main__':
    result = Solution()
    s = "abcabcbb"
    ans = result.lengthOfLongestSubstring2(s)
    print(ans)
