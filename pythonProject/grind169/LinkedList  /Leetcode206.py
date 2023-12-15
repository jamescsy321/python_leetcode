from typing import List, Optional


# from pythonProject.grind169 import ListNode
# 206. Reverse Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # iterative
    '''
    exmple:1->2->3->4->5

    prev=None
    1.
    nxt = head.next => nxt = 2345 head =12345
    head.next =prev => head.next =None / head = 1,None
    prev = head     => prev = 1,None
    head = nxt      => head = 2345
    2.
    nxt = head.next => nxt = 345 head =2345
    head.next =prev => head.next =1,None / head = 2,1,None
    prev = head     => prev = 2,1,None
    head = nxt      => head = 345
    3.
    nxt = head.next => nxt = 45 head =345
    head.next =prev => head.next =2,1,None / head = 3,2,1,None
    prev = head     => prev = 3,2,1,None
    head = nxt      => head = 45
    以此類推
    '''
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            next_node = head.next
            # 將向後指針轉向指向前,1->0,2->1->0
            head.next = prev
            # 更新完指針後將prev更新為head
            prev = head
            # 將指針移位
            head = next_node
        return prev

    # recursive
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if not head or not head.next:
            return head

        revese_list_head = self.reverseList2(head.next)
        head.next.next = head
        head.next = None
        return revese_list_head


if __name__ == '__main__':
    result = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    previous = head
    while previous is not None:
        print(previous.val)
        previous = previous.next
    ans = result.reverseList(head)

    current = ans
    while current is not None:
        print(current.val)
        current = current.next
