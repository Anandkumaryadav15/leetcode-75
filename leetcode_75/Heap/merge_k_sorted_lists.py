from typing import List, Optional
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Problem: Merge K Sorted Lists
    
    You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
    Merge all the linked-lists into one sorted linked-list and return it.
    
    Time Complexity: O(N log k)
    - Where N is the total number of nodes and k is the number of lists.
    - Each insertion/removal from the heap takes O(log k).
    
    Space Complexity: O(k)
    - To store the heap with k elements.
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        
        # Add head of each list to the min heap
        for i in range(len(lists)):
            if lists[i]:
                # Store tuple (val, index, node)
                # index is used to break ties if values are equal (since ListNode is not directly comparable < without custom __lt__)
                heapq.heappush(minHeap, (lists[i].val, i, lists[i]))
                
        dummy = ListNode()
        tail = dummy
        
        while minHeap:
            # Pop the smallest node
            val, i, node = heapq.heappop(minHeap)
            tail.next = node
            tail = tail.next
            
            # If there is a next node in that list, push it to heap
            if node.next:
                heapq.heappush(minHeap, (node.next.val, i, node.next))
                
        return dummy.next
