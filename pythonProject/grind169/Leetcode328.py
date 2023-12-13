from typing import Optional


# 328. Odd Even Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        odd, even, even_head = head, head.next, head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head

    def oddEvenList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 先檢查節點是否存在
        if not head:
            return head
        # 設三個指針，e_head記錄even的起始位置，因為之後要加奇數尾端連到雙數頭端
        # odd 和 even 都指向鏈表的起始位置，even 則指向 head 的下一個節點
        odd = head
        even = head.next
        even_head = even
        # 將原本的節點只到下一個節點的下一個節點
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            # 移動奇數跟雙數指針到下一個位置
            odd = odd.next
            even = even.next
        # 最後將奇數尾最後節點指到偶數節點的起始位置
        odd.next = even_head
        return head
