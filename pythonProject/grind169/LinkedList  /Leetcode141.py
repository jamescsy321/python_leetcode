from typing import Optional


# 141. Linked List Cycle
# fast and slow pointer 使用快慢指針，如果有循環總有一天會碰到
# Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
