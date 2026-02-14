from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Problem: Remove Nth Node From End Of List
    
    Given the head of a linked list, remove the nth node from the end of the list and return its head.
    
    Time Complexity: O(n)
    - Single pass using two pointers.
    
    Space Complexity: O(1)
    - Constant extra space.
    """
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Dummy node to handle edge case where head needs to be removed
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # Move right pointer n steps ahead
        while n > 0 and right:
            right = right.next
            n -= 1
            
        # Move both pointers until right reaches the end
        while right:
            left = left.next
            right = right.next
            
        # Now left is at the node BEFORE the one we want to delete
        left.next = left.next.next
        
        return dummy.next
