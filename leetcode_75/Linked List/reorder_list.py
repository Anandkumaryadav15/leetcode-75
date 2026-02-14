from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Problem: Reorder List
    
    You are given the head of a singly linked-list. The list can be represented as:
    L0 -> L1 -> ... -> Ln - 1 -> Ln
    Reorder the list to be on the following form:
    L0 -> Ln -> L1 -> Ln - 1 -> L2 -> Ln - 2 -> ...
    You may not modify the values in the list's nodes. Only nodes themselves may be changed.
    
    Time Complexity: O(n)
    - 1. Find middle O(n)
    - 2. Reverse second half O(n)
    - 3. Merge two halves O(n)
    
    Space Complexity: O(1)
    - In-place manipulation.
    """
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
            
        # 1. Find middle using slow/fast pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 2. Reverse the second half
        second = slow.next
        prev = slow.next = None # Split the list
        
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # 3. Merge the two halves
        # first half head is 'head', second half head is 'prev'
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
