# Results:
# Runtime: 41ms 74.54%
# Memory Usage: 15.5MB 54.69%

"""

https://leetcode.com/problems/reverse-linked-list/

Idea:
- if you iterate thru list, will receive nodes in reverse order, so new nodes become new head
- maintain currentHead pointer
- O(n) time, O(1) space. optimal

Idea2:
- handle prev, curr, next, and connect and iterate.

Tactic
can build the reverse list from the entries in order. keep growing head

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverseList(self, head):
        if (head is None or head.next is None):
            return head

        prev = None
        curr = head

        while (curr is not None):
            # connect curr with prev
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return prev
        


    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = None

        while (head != None):
            currNode = ListNode(head.val, head.next)

            if (newHead == None):
                newHead = currNode
                newHead.next = None
            else:
                currNode.next = newHead
                newHead = currNode
            
            head = head.next
        
        return newHead
        

        
