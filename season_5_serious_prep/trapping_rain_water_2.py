"""

Ideas:
- bfs from each level, see how many are enclosed and update
- sort by heights first
- each one found, mark as discovered

O(heights * mn) + O(mn log mn)

too slow

Something to do with heap??

Idea 2:
- sort first by height
- start search from smallest height, only expand by smallest
- keep monotonic decreasing list with (height, idx) of largest seen and also visited array?
- once hit water, then can know all heights of visited squares. go thru and fill out.
- if you hit a pre-searched square -> end search. That's max height seen, everything smaller nearby 
would have been searched

Idea 3:
- search from edges
- explore next from smallest edge - can deduce

"""

import heapq

def solve(heights):
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def isOutOfBounds(r, c):
        return r < 0 or r >= len(heights) or c < 0 or c >= len(heights[0])
    
    total = 0
    to_search = []
    processed = set()
    added_to_search = set()
    
    
    for r in range(len(heights)):
        heapq.heappush(to_search, (heights[r][0], r, 0))
        heapq.heappush(to_search, (heights[r][-1], r, len(heights[0]) - 1))
        added_to_search.add((r, 0))
        added_to_search.add((r, len(heights[0]) - 1))
    for c in range(1, len(heights[0]) - 1):
        heapq.heappush(to_search, (heights[0][c], 0, c))
        heapq.heappush(to_search, (heights[-1][c], len(heights) - 1, c))
        added_to_search.add((heights[0][c], 0, c))
        added_to_search.add((heights[-1][c], len(heights) - 1, c))
    
    def getWater(h, r, c):
        nonlocal directions
        nonlocal processed
        min_neigh = float('inf')
        for dr, dc in directions:
            if isOutOfBounds(r + dr, c + dc):
                return h
            if (r + dr, c + dc) not in processed: continue
            min_neigh = min(min_neigh, heights[r + dr][c + dc]) # take min of processed heights
        
        return h if min_neigh == float('inf') else max(h, min_neigh)
    
    while to_search:
        h, r, c = heapq.heappop(to_search) # pop min

        wat = getWater(h, r, c)
        total += wat - h
        heights[r][c] = wat

        processed.add((r, c))

        for dr, dc in directions:
            if isOutOfBounds(r + dr, c + dc): continue
            if (r + dr, c + dc) not in added_to_search:
                heapq.heappush(to_search, (heights[r+dr][c+dc], r + dr, c + dc))
                added_to_search.add((r + dr, c + dc))
    
    return total

    
print(solve([[2, 2, 2], [2, 1, 2], [2, 2, 2]]))
print(solve([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]))
print(solve([[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]))
print(solve([[78,16,94,36],[87,93,50,22],[63,28,91,60],[64,27,41,27],[73,37,12,69],[68,30,83,31],[63,24,68,36]]))
print(solve([[14,17,18,16,14,16],[17,3,10,2,3,8],[11,10,4,7,1,7],[13,7,2,9,8,10],[13,1,3,4,8,6],[20,3,3,9,10,8]]))



import heapq

def solve(heights):
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def isOutOfBounds(r, c):
        return r < 0 or r >= len(heights) or c < 0 or c >= len(heights[0])
    
    # -1 for not solved yet
    # see currentSearch for set of elts in current search
    water = [[-1 for _ in range(len(heights[0]))] for _ in range(len(heights))]

    def isSolved(r, c):
        nonlocal water
        return water[r][c] >= 0
    
    # Returns last node searched (could be first one out), and visited set
    def search(row, col):
        nonlocal water
        nonlocal directions
        # Step 1: explore from row, col
        to_search = [(heights[row][col], row, col)]
        currentSearch = set() # elts to search
        currentSearch.add((row, col))
        searched = set() # searched elts
        # print("start search", water)

        last = (row, col) # to return

        while to_search:
            h, r, c = heapq.heappop(to_search) # take min
            # print(r, c, "asdf")
            
            if isSolved(r, c):
                # print("solved", r, c)
                last = (r, c) # special case, if last is not in visited! since already solved
                break
            
            # added to this search
            last = (r, c)
            searched.add((r, c))

            # Add neighbouring cells
            isOut = False
            for dr, dc in directions:
                if isOutOfBounds(r + dr, c + dc): # if out of bounds, finished
                    isOut = True
                    break
                elif (r + dr, c + dc) in currentSearch:
                    continue # Don't add already added
                heapq.heappush(to_search, (heights[r + dr][c + dc], r + dr, c + dc)) # Add
                currentSearch.add((r + dr, c + dc))
            if isOut:
                break
        
        return last, searched
    
    def get_min_neighbour_water(r, c, visited):
        nonlocal water
        nonlocal directions
        min_neigh = float('inf')
        for dr, dc in directions:
            if isOutOfBounds(r + dr, c + dc): return float('-inf')
            elif water[r + dr][c + dc] == -1:
                if (r + dr, c + dc) in visited: continue
                min_neigh = min(min_neigh, heights[r + dr][c + dc]) # water score will be -1 if unsolved
            else:
                min_neigh = min(min_neigh, water[r + dr][c + dc]) # water score will be -1 if unsolved
        return min_neigh if min_neigh != float('inf') else float('-inf')

    def fill(startR, startC, visited):
        nonlocal water
        to_fill = [(heights[startR][startC], startR, startC)]
        other_visited = visited.copy()
        if (startR, startC) in visited:
            visited.remove((startR, startC)) # remove from search, do not add again
        # print(water)
        # print(visited)

        while to_fill:
            h, r, c = heapq.heappop(to_fill)
            # print(r, c)
            # assert(water[r][c] == -1)
            # print(r, c, h, get_min_neighbour_water(r, c, other_visited))
            if water[r][c] == -1: # could be already filled
                water[r][c] = max(h, get_min_neighbour_water(r, c, other_visited))
            # add next
            for dr, dc in directions:
                if (r + dr, c + dc) in visited:
                    heapq.heappush(to_fill, (heights[r + dr][c + dc], r + dr, c + dc))
                    visited.remove((r + dr, c + dc)) # so not added again
        # print("after")
        # for r in water: print(r)
    
    for r in range(len(heights)):
        for c in range(len(heights[0])):
            if isSolved(r, c): continue
            (rs, cs), visited = search(r, c)
            fill(rs, cs, visited)
    
    total = 0
    for r in range(len(heights)):
        for c in range(len(heights[0])):
            assert(water[r][c] >= 0)
            total += water[r][c] - heights[r][c]
            heights[r][c] = water[r][c] - heights[r][c]
    # for r in heights: print(r)
    return total
    
# print(solve([[2, 2, 2], [2, 1, 2], [2, 2, 2]]))
# print(solve([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]))
# print(solve([[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]))
# print(solve([[78,16,94,36],[87,93,50,22],[63,28,91,60],[64,27,41,27],[73,37,12,69],[68,30,83,31],[63,24,68,36]]))
# print(solve([[14,17,18,16,14,16],[17,3,10,2,3,8],[11,10,4,7,1,7],[13,7,2,9,8,10],[13,1,3,4,8,6],[20,3,3,9,10,8]]))

[[14,17,18,16,14,16],
 [17,3 ,10,2 ,3,8],
 [11,10,4,7,1,7],
 [13,7,2,9,8,10],
 [13,1,3,4,8,6],
 [20,3,3,9,10,8]]


# import heapq

# def solve(heights):

#     def isOutOfBounds(r, c):
#         return r < 0 or r >= len(heights) or c < 0 or c >= len(heights[0])

#     # (r, c) not visited yet. So search using min from here.
#     # if encounter another visited, can terminate search and go thru history 
#     # to add heights
#     def search(visited, row, col):
#         # if (row, col) in visited: return
#         history = []
#         max_heights_seen = [] # (height, idx) - this idx and before have this max. 
#         to_search = [(heights[row][col], row, col)]

#         visited_this_search = set()
#         added_this_search = set([(row, col)])
#         while to_search:
#             h, r, c = heapq.heappop(to_search) # take min
#             print(r, c, h)
#             print("mhs", max_heights_seen)

#             if not max_heights_seen:
#                 max_heights_seen.append((h, len(history)))
#             elif h >= max_heights_seen[-1][0]: # Technically don't need to handle equals case
#                 idx = len(history)
#                 while max_heights_seen and h > max_heights_seen[-1][0]:
#                     h2, idx = max_heights_seen.pop()
#                 max_heights_seen.append((h, idx))
#             elif h < max_heights_seen[-1][0]: # need to add new entry
#                 max_heights_seen.append((h, len(history))) # from idx, h is the max seen

#             print("mh2", max_heights_seen)
#             print(r, c, visited)

#             if (r, c) in visited:
#                 print("Visited??:", r, c, visited)
#                 # kludge fix to correct when adding last that's already visited
#                 if max_heights_seen and max_heights_seen[-1][1] == len(history):
#                     max_heights_seen.pop()

#                 break
                
#             visited_this_search.add((r, c))
            
#             # Add to history
#             history.append(h) # history only cares about height
#             print("hist:", history)

#             # Add neighbouring cells
#             isOut = False
#             for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
#                 if isOutOfBounds(r + dr, c + dc):
#                     isOut = True
#                     break
#                 elif (r + dr, c + dc) in added_this_search: continue # Don't add
#                 heapq.heappush(to_search, (heights[r + dr][c + dc], r + dr, c + dc))
#                 added_this_search.add((r + dr, c + dc))
#             if isOut:
#                 break
        
#         # Search over, so found final. Now go thru and add heights
#         print([(idx, h) for idx, h in enumerate(history)])
#         print(max_heights_seen)


#         idx = len(history) - 1
#         total = 0
#         while history:
#             if max_heights_seen[-1][1] > idx:
#                 max_heights_seen.pop()
#             h = history.pop()
#             print(max_heights_seen, h)
#             total += max_heights_seen[-1][0] - h
#             idx -= 1
#         print(total)
#         print("adding", visited_this_search)

#         for r, c in visited_this_search:
#             visited.add((r, c))
#         return total
    
#     total = 0
#     visited = set()
#     for r in range(len(heights)):
#         for c in range(len(heights[0])):
#             # print(visited)
#             print("searching", r, c)
#             total += search(visited, r, c)
#     return total


# print(solve([[2, 2, 2], [2, 1, 2], [2, 2, 2]]))
# print(solve([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]))
# print(solve([[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]))
# print(solve([[78,16,94,36],[87,93,50,22],[63,28,91,60],[64,27,41,27],[73,37,12,69],[68,30,83,31],[63,24,68,36]]))



def solve(heights):

    # custom exn
    class FlowOutOfBounds(Exception):
        pass

    sortedHeights = set()

    for r in range(len(heights)):
        for c in range(len(heights[0])):
            sortedHeights.add(heights[r][c])
    sortedHeights = sorted(sortedHeights, reverse=True)

    # now go in decreasing order of heights, dfs
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def isOutOfBounds(r, c):
        return not (0 <= r and r < len(heights) and 0 <= c and c < len(heights[0]))

    # Returns total depth
    # if out of bounds, sets isLeaking to True and continues search.
    def dfs(height, r, c, visited, visitedThisRun, isLeaking): # visited keeps tickets
        if isOutOfBounds(r, c):
            isLeaking[0] = True
            return 0

        if (r, c) in visited:
            return 0
        
        if heights[r][c] >= height:
            return 0 # early return since cannot contribute anything, do not continue exploring

        totalDepth = height - heights[r][c]
        visited.add((r, c))
        visitedThisRun.add((r, c))

        for dr, dc in directions:
            totalDepth += dfs(height, r + dr, c + dc, visited, visitedThisRun, isLeaking)

        return totalDepth
    
    total = 0
    visitedInGeneral = set()
    for h in sortedHeights:
        visited = set()
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r, c) not in visited and (r, c) not in visitedInGeneral and heights[r][c] < h:
                    isLeaking = [False]
                    visitedThisRun = set()
                    amt = dfs(h, r, c, visited, visitedThisRun, isLeaking)
                    if not isLeaking[0]:
                        total += amt # leaked
                        for x in visitedThisRun:
                            visitedInGeneral.add(x)


    return total

# l solve([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]])
# print(solve([[78,16,94,36],[87,93,50,22],[63,28,91,60],[64,27,41,27],[73,37,12,69],[68,30,83,31],[63,24,68,36]]))

# [78,16,94,36],
# [87,93,50,22],
# [63,28,91,60],
# [64,27,41,27],
# [73,37,12,69],
# [68,30,83,31],
# [63,24,68,36]]