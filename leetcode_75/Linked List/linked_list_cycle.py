from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    Problem: Detect Cycle in a Linked List
    
    Given head, the head of a linked list, determine if the linked list has a cycle in it.
    
    Time Complexity: O(n)
    - Floyd's Cycle Detection Algorithm (Tortoise and Hare).
    
    Space Complexity: O(1)
    - We only use two pointers.
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next          # Move slow pointer by 1
            fast = fast.next.next     # Move fast pointer by 2
            
            # If they meet, there is a cycle
            if slow == fast:
                return True
                
        return False
