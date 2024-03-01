# 125. Valid Palindrome
# easy
# 使用雙指針，前後各一去比對
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j:
            # isalnum（）方法檢查字符串是否為空，如果為空則跳過
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1
        return True

if __name__ == '__main__':
    result = Solution()
    s = "A man, a plan, a canal: Panama"
    ans = result .isPalindrome(s)
    print(ans)


