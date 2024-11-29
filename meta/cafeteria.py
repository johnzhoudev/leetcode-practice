"""


N seats
k seats to left and right (or remaining seats if end)
m diners, ith is in seat s[i], social distancing satisfied

how many more can be sat down?

Greedy solution?

S = [2, 6]

_ x _ _ _ x _ _ _ _

greedily sit down on leftmost one
- If you can sit in a seat, there's no point not sitting in that seat if it's the leftmost

O(n) time just greedily go down and sit when u can
O(1) space

need to just find range where there's no sitters

O(n m) time

O(n) time easy

Better: Intervals?
- find out sizes of all intervals
- calculate max number of things you can sit in per interval, since intervals cannot affect each otehr (separated by others)
  - interval length / k + 1 ceiling

Tactic: Double pointer sliding window slow. Instead, figure out free interval length and calculate how many diners can be added. O(m) time.
_ _ _ _ _ _ _ _
"""

from math import ceil

def solve(n, k, m, s):
  previousEnd = 0 # inclusive, cannot be used
  # get intervals
  s.sort()
  totalAdded = 0

  def calculateTotalAdded(left, right):
    sizeOfInterval = right - left + 1
    if sizeOfInterval > 0:
      return int(ceil(float(sizeOfInterval) / (k + 1)))
    return 0

  for center in s:
    # figure out size of left interval
    totalAdded += calculateTotalAdded(previousEnd + 1, center - k - 1)
    previousEnd = center + k
  
  # calculate for last interval to end of n
  totalAdded += calculateTotalAdded(previousEnd + 1, n)
  
  return totalAdded


def solve(n, k, m, s) -> int:

  newDiners = 0
  seatsTaken = set(s)

  curr = 1
  left = curr - k
  right = curr + k

  numSeatsTaken = 0
  for i in range(1, right + 1):
    if i in seatsTaken: numSeatsTaken += 1

  while curr <= n:
    if numSeatsTaken == 0:
      seatsTaken.add(curr)
      newDiners += 1
      numSeatsTaken += 1
    if (left in seatsTaken): numSeatsTaken -= 1
    left += 1
    curr += 1
    right += 1
    if (right in seatsTaken): numSeatsTaken += 1
  
  return newDiners



def solve(n, k, m, s) -> int:
  newDiners = 0
  seatsTaken = set(s)

  def isValidRange(start, end):
    for i in range(max(start, 1), min(end + 1, n + 1)):
      if i in seatsTaken: return False
    return True

  for i in range(1, n + 1):
    if isValidRange(i - k, i + k):
      seatsTaken.add(i)
      newDiners += 1
  
  return newDiners
  


