from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Problem: Reverse Linked List
    
    Given the head of a singly linked list, reverse the list, and return the reversed list.
    
    Time Complexity: O(n)
    - We traverse the list exactly once.
    
    Space Complexity: O(1)
    - Iterative approach uses constant extra space.
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        
        while curr:
            # Save the next node
            nxt = curr.next
            # Reverse the pointer
            curr.next = prev
            # Move prev and curr forward
            prev = curr
            curr = nxt
            
        return prev
