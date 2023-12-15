
# 232. Implement Queue using Stacks
# stack

class MyQueue:

    def __init__(self):
        self.in_stk = []
        self.out_stk = []

    def push(self, x: int) -> None:
        self.in_stk.append(x)

    def pop(self) -> int:
        self.peek()
        return self.out_stk.pop()

    def peek(self) -> int:
        # 如果 out_stk 是空的，程式將從 in_stk 中將元素逐一彈出，並推入 out_stk 中
        # ，這樣 out_stk 中的元素順序就會與 in_stk 相反，即最先進入的元素會在 out_stk 的頂端。
        # 然後返回 out_stk 的最頂端元素，即為佇列的第一個元素。
        if not self.out_stk:
            while self.in_stk:
                self.out_stk.append(self.in_stk.pop())
        return self.out_stk[-1]

    def empty(self) -> bool:
        return not self.in_stk and not self.out_stk
