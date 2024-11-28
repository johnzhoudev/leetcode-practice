"""

Director of Photography (Chapter 1)

n cells in a row
P = photo
A = actor
B = backdrop
. = empty

artistic if dist between photo and actor is [X, Y] 
and dist between actor and backdrop
dist = |i-j|

Number of artistic photographs?


Idea:
- given actor location
- number of artistic is num spots to left with valid photo * right with valid backdrop - preprocess
- and right / left

Preprocess step: 
moving right, make array with number of photo / actor 
moving left, make array of seen

Tactic:
Preprocess, count number of photo / backdrop to left / to right

"""

from collections import defaultdict

def solve(n, s, X, Y):

  # Preprocess
  photoToLeft = [0 for _ in range(len(s))]
  backdropToLeft = [0 for _ in range(len(s))]
  photoToRight = [0 for _ in range(len(s))]
  backdropToRight = [0 for _ in range(len(s))]

  counts = defaultdict(lambda : 0)
  # left to right
  for idx, c in enumerate(s):
    counts[c] += 1
    photoToLeft[idx] = counts['P']
    backdropToLeft[idx] = counts['B']
  
  # backwards
  counts.clear()
  for i in range(len(s) - 1, -1, -1):
    counts[s[i]] += 1
    photoToRight[i] = counts['P']
    backdropToRight[i] = counts['B']

  # Now have preprocessed data, so count

  totalWays = 0

  # returns (photos to left, backdrop to left)
  def getNumPhotoBackdropToLeft(leftIdx, largerLeftIdx):
    if (leftIdx < 0): return (0, 0) # out of bounds
    if (largerLeftIdx - 1 < 0): # to end
      return (photoToLeft[leftIdx], backdropToLeft[leftIdx])
    return (photoToLeft[leftIdx] - photoToLeft[largerLeftIdx - 1], backdropToLeft[leftIdx] - backdropToLeft[largerLeftIdx - 1])
  
  def getNumPhotoBackdropToRight(rightIdx, largerRightIdx):
    if (rightIdx >= len(s)): return (0, 0) # out of bounds
    if (largerRightIdx + 1 >= len(s)): # to end
      return (photoToRight[rightIdx], backdropToRight[rightIdx])
    return (photoToRight[rightIdx] - photoToRight[largerRightIdx + 1], backdropToRight[rightIdx] - backdropToRight[largerRightIdx + 1])

  for actorIdx in range(len(s)):
    if (s[actorIdx] != 'A'): continue

    # x <= |b-a| <= Y
    # so a + x is x distance away
    # a + y is y distance away

    leftIdx = actorIdx - X # could be < 0
    largerLeftIdx = max(actorIdx - Y, 0) # take until 0
    rightIdx = actorIdx + X # could be >= len(s)
    largerRightIdx = min(actorIdx + Y, len(s) - 1)


    lPhotos, lBackdrop = getNumPhotoBackdropToLeft(leftIdx, largerLeftIdx)
    rPhotos, rBackdrop = getNumPhotoBackdropToRight(rightIdx, largerRightIdx)


    totalWays += lPhotos * rBackdrop
    totalWays += rPhotos * lBackdrop
  
  return totalWays


print(solve(8, ".PBAAP.B", 1, 3))