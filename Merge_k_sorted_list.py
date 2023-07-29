import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_sorted_lists(lists):
    heap = []
    for head in lists:
        while head:
            heapq.heappush(heap, head.val)
            head = head.next

    dummy = ListNode()
    current = dummy
    while heap:
        smallest = heapq.heappop(heap)
        current.next = ListNode(smallest)
        current = current.next

    return dummy.next


# Example usage:
# Constructing the sorted linked lists:
# List 1: 1 -> 4 -> 5
# List 2: 1 -> 3 -> 4
# List 3: 2 -> 6
list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))

sorted_list = merge_k_sorted_lists([list1, list2, list3])
# Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
while sorted_list:
    print(sorted_list.val, end=" -> ")
    sorted_list = sorted_list.next
print("None")
