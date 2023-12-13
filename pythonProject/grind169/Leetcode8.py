import re


# 8. String to Integer (atoi)
class Solution:
    # 使用正則的方式
    def myAtoi(self, str: str) -> int:
        int_max = 2147483647
        int_min = -2147483648

        val_str = re.match('(^[\-]?\d+)', str.strip())

        if not val_str:
            return 0
        val = int(val_str.group(0))
        val = min(int_max, max(int_min, val))
        return val

    def myAtoi2(self, str: str) -> int:
        # 定義了整數的最大值和最小值，超出這個範圍的數字會被截斷為最大值或最小值。
        int_max = 2147483647
        int_min = -2147483648
        # 移除字串兩端的空白字符
        str = str.strip()
        if len(str) == 0:
            return 0
        # sign 記錄正負號，初始值為 1（正數）。如果字串的第一個字符為 - 或 +，則將 sign 設置為 -1 或 1，並將該字符從字串中去除。
        sign = 1
        val = 0
        if str[0] in ["-", "+"]:
            sign = 1 if str[0] == "+" else -1
            str = str[1:]
        '''
        ord() 是 Python 中的一個內建函數，用於獲取字符的 ASCII 碼值。在這段程式碼中，它的作用是將給定的字符轉換為其對應的 ASCII 數值。
        在程式碼中，ord(char) - ord("0") 的部分則是將字串中的數字字符轉換為對應的數值。因為 ASCII 中數字字符是連續的，
        所以將字符減去 '0' 的 ASCII 值（即 48）可以得到該數字字符表示的數字值。這樣就可以將字符 '0' 到 '9' 轉換為整數 0 到 9。
        例如，假設 char 是 '5'，則 ord(char) 返回的是 53，ord(char) - ord("0") 返回的是 53 - 48 = 5，這樣就把字符 '5' 轉換為整數 5。
        使用迴圈處理字串中的每個字符：
        如果該字符不是數字，則跳出迴圈。
        如果是數字字符，將其轉換為數字並更新 val 變量。這裡使用了 ASCII 碼的轉換方式：將字符轉換為對應的數字值。
        最後，返回 val * sign 的值，但會確保結果在 int_max 和 int_min 之間，防止溢出
        '''
        for char in str:
            if not char.isdigit():
                break
            val = val * 10 + ord(char) - ord("0")

        return min(int_max, max(int_min, val * sign))


if __name__ == '__main__':
    result = Solution()
    s = "4193 with words"
    ans = result.myAtoi(s)
    print(ans)
