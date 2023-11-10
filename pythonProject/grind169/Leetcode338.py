from typing import List


# 求到n之前的每各位數的1的數量

def countBits(n: int) -> List[int]:
    counter = [0]
    for i in range(1, n + 1):
        demo = counter[i >> 1]
        counter.append(counter[i >> 1] + i % 2)
    return counter


if __name__ == '__main__':
    result = countBits(5)
    print(result)

# 這段程式碼是一個Python函式，看起來是一個類的方法，可能是LeetCode題目的一部分。它的目標是計算從0到`num`這個整數範圍內每個數字的二進制表示中有多少個1。以下是對程式碼的詳細解釋：
#
# 1. 函式簽名: `countBits(self, num: int) -> List[int]`，這個函式接受一個整數`num`作為參數，然後返回一個整數列表（`List[
# int]`），列表中包含了0到`num`每個數字的二進制表示中1的個數。
#
# 2. 創建一個名為`counter`的列表，初始只包含一個元素0，這是因為0的二進制表示中只有一個1。
#
# 3. 使用`for`迴圈，從1遍歷到`num`（包含`num`本身）。
#
# 4. 在迴圈中，計算每個數字的二進制表示中1的個數。這是通過`counter[i >> 1] + i % 2`來實現的：
#    - `i >> 1`：這將`i`右移一位，等同於將`i`的二進制表示向右移動一位，這樣可以獲得`i`的一半。
#    - `i % 2`：這將`i`除以2取餘數，如果`i`是奇數，結果為1，如果`i`是偶數，結果為0。
#    - `counter[i >> 1] + i % 2`：將`i`的一半的1的個數（`counter[i >> 1]`）和`i`是否是奇數的結果相加，以計算`i`的二進制表示中1的個數。
#
# 5. 然後將計算得到的1的個數添加到`counter`列表中。
#
# 6. 最終，函式返回填充完整的`counter`列表，其中包含0到`num`每個數字的二進制表示中1的個數。
