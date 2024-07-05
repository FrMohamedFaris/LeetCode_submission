class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode:

        ptr1 = head
        ptr2 = head.next
        s = 0

        while ptr2:
            if ptr2.val == 0:

                ptr1 = ptr1.next
                ptr1.val = s
                s = 0
            else:
                s += ptr2.val
            ptr2 = ptr2.next

        ptr1.next = None

        return head.next


def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def print_linked_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    print(result)


head = create_linked_list([0, 3, 1, 0, 4, 5, 2, 0])
solution = Solution()
modified_head = solution.mergeNodes(head)
print_linked_list(modified_head)
