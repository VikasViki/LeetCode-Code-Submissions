# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def get_total_nodes(self, node):
        curr = node
        count = 0
        while curr:
            curr = curr.next
            count += 1
        return count

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        total_nodes = self.get_total_nodes(head)
        if total_nodes <= 1: return head

        k = k % total_nodes
        if k == 0: return head

        curr = head
        for _ in range(k):
            curr = curr.next

        start = head
        k_node = curr
        while k_node.next:
            k_node = k_node.next
            start = start.next
        
        new_head = start.next # setting new head after K rotation
        start.next = None # Breaking list for new tail
        k_node.next = head

        return new_head