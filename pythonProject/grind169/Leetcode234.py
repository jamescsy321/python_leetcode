from pythonProject.grind169 import ListNode
from typing import Optional


def isPalindrome(head: Optional[ListNode]) -> bool:

    fast = head
    slow = head
    # find middle(slow)
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    # reverse second half
    prev = None
    while slow:
        tmp = slow.next
        slow.next = prev
        prev = slow
        slow = tmp

    # check palindrome
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True

# if __name__ == '__main__':
