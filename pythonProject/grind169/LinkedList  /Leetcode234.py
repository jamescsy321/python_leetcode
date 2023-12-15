from typing import Optional


# 234. Palindrome Linked List
# Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

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


    # 使用快慢指針，指到中間時將後面部分反轉後比較
    def isPalindrome2(head: Optional[ListNode]) -> bool:
        def find_middle(head: ListNode) -> ListNode:
            slow = fast = head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow

        def reverse_linked_list(head: ListNode) -> ListNode:
            prev = None
            while head:
                next_node = head.next
                head.next = prev
                prev = head
                head = next_node
            return prev

        #     edge
        if not head or not head.next:
            return True

        first_half = find_middle(head)
        second_half = reverse_linked_list(first_half)

        while head and second_half:
            if head.val != second_half.val:
                return False
            head = head.next
            second_half = second_half.next
        return True


if __name__ == '__main__':
    result = Solution()
    head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    ans = result.isPalindrome2(head)
    print(ans)
