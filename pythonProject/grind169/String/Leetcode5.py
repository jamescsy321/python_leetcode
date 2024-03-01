# 5. Longest Palindromic Substring
# stock,DP
class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = ''

        for i in range(len(s)):
            # example "babad" 以a為起點所以左右都設i
            len1 = len(self.getlongestpalindrome(s, i, i))

            if len1 > len(palindrome):
                palindrome = self.getlongestpalindrome(s, i, i)
            # example "cbbd" ,output=bb的話假設左b為起點所以右設i+1
            len2 = len(self.getlongestpalindrome(s, i, i + 1))

            if len2 > len(palindrome):
                palindrome = self.getlongestpalindrome(s, i, i + 1)

        return palindrome

    def getlongestpalindrome(self, s, left, right):
        # 從中間往左右擴展
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        #     回傳s[start:end]之間的字串
        return s[left + 1:right]


if __name__ == '__main__':
    result = Solution()
    s = "babad"
    ans = result.longestPalindrome(s)
    print(ans)
