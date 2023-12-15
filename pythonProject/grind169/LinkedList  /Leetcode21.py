from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 21. Merge Two Sorted Lists
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    cur = dummy = ListNode(0)
    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next
        cur = cur.next

    cur.next = list1 or list2

    return dummy.next


def print_linked_list(head):
    values = []
    while current:
        values.append(current.val)
        current = current.next
    print(values)


if __name__ == '__main__':
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)

    result = mergeTwoLists(list1, list2)
    while result is not None:
        print(result.val)
        result = result.next
