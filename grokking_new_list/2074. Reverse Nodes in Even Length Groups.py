"""

2074. Reverse Nodes in Even Length Groups
https://leetcode.com/problems/reverse-nodes-in-even-length-groups/description/

Idea:
- have alg for reverse(x, n) - returns head
- have alg for skipping

O(n) time, O(1) space

Tactic: Lookahead function to determine real length, and reverse helper returning head and last elt. Keep prev too.

"""

def solve(head):

  def dumpList(h):
    print("dumping")
    while h:
      print(h.val)
      h = h.next

  def lookahead(h, n):
    count = 0
    while h and count < n:
      count += 1
      h = h.next
    return count


  def reverse(head, n): # returns head, tail (last elt)
    accumulator = None
    end = None
    for _ in range(n):
      if head is None: break
      curr = head
      head = head.next
      curr.next = accumulator
      if not end: end = curr
      accumulator = curr
    
    # Now attach tail
    tail = head
    end.next = tail
    return accumulator, end
  
  n = 1
  start = head
  prev = None
  while head:
    n = lookahead(head, n)

    if n % 2 == 0: # if even, reverse
      # reverse
      newHead, tail = reverse(head, n)
      prev.next = newHead
      prev = tail

      if tail:
        head = tail.next
      
    else:
      # Just continue
      for _ in range(n):
        if not head: break
        prev = head
        head = head.next

    n += 1
    
  return start

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
x = (solve(ListNode(1, ListNode(1, ListNode(0, ListNode(6, ListNode(5)))))))

while x:
  print(x.val)
  x = x.next



  





    
