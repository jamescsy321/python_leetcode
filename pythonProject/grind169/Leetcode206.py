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
    nxt = current   => nxt = 2345 curr =12345
    curr.next =prev => curr.next =None / curr = 1,None
    prev = curr     => prev = 1,None
    curr = nxt      => curr = 2345
    2.
    nxt = current   => nxt = 345 curr =2345
    curr.next =prev => curr.next =1,None / curr = 2,1,None
    prev = curr     => prev = 2,1,None
    curr = nxt      => curr = 345
    3.
    nxt = current   => nxt = 45 curr =345
    curr.next =prev => curr.next =2,1,None / curr = 3,2,1,None
    prev = curr     => prev = 3,2,1,None
    curr = nxt      => curr = 45
    以此類推
    '''
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr =head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
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
