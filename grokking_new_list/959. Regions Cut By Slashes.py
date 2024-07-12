"""

959. Regions Cut By Slashes
https://leetcode.com/problems/regions-cut-by-slashes/description/

Ideas:
- dfs from each point, if adjacent not separated by slash, then one region
- count number of regions

- hold up, slashes make diff regions
- each square has top and bottom, connected by left and right
- so still dfs, but visited has diff

- Yolo, make a new graph
- node - 

O(n) time, O(n) space (to store visited set)

Tactic: Either create new graph manually, or upscale 3x3

"""

# Upscale method to 3x3
def solve(grid):
  n = len(grid)

  # upscale
  newGrid = [[' ' for _ in range(3*n)] for _ in range(3 *n)]
  for i in range(n):
    for j in range(n):
      if grid[i][j] == '\\':
        newGrid[i*3][j*3] = '\\'
        newGrid[i*3 + 1][j*3 + 1] = '\\'
        newGrid[i*3 + 2][j*3 + 2] = '\\'
      elif grid[i][j] == '/':
        newGrid[i*3][j*3 + 2] = '/'
        newGrid[i*3 + 1][j*3 + 1] = '/'
        newGrid[i*3 + 2][j*3] = '/'
  
  visited = [[False for _ in range(3*n)] for _ in range(3*n)]

  directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
  def dfs(i, j):
    if i < 0 or i >= 3 * n or j < 0 or j >= 3*n: return
    if visited[i][j]: return
    if newGrid[i][j] != ' ': return
    visited[i][j] = True
    for dx, dy in directions:
      dfs(i + dx, j + dy)
  
  numIslands = 0
  for i in range(3 * n):
    for j in range(3 * n):
      if visited[i][j] or newGrid[i][j] != ' ': continue
      numIslands += 1
      dfs(i, j)
  
  return numIslands



class Node():
  def __init__(self):
    self.next = [] # array of node references

def solve(grid):
  n = len(grid)
  
  # First make new graph
  newGrid = [[None for _ in range(n)] for _ in range(n)] # make new node for each
  for i in range(n):
    for j in range(n):
      newGrid[i][j] = [Node()] if grid[i][j] == ' ' else [Node(), Node()] # Top, bottom
  
  def goUp(i, j): # returns node
    j = j - 1
    if j < 0: return None
    if grid[i][j] == ' ': return newGrid[i][j][0]
    else: return newGrid[i][j][1] # bottom
  
  def goDown(i, j): # returns node
    j = j + 1
    if j >= n: return None
    if grid[i][j] == ' ': return newGrid[i][j][0]
    else: return newGrid[i][j][0] # bottom

  def goLeft(i, j): # returns node
    i = i - 1
    if i < 0: return None
    if grid[i][j] == ' ': return newGrid[i][j][0]
    if grid[i][j] == '\\': return newGrid[i][j][0] # Top
    else: return newGrid[i][j][1]
  
  def goRight(i, j): # returns node
    i = i + 1
    if i >= n: return None
    if grid[i][j] == ' ': return newGrid[i][j][0]
    if grid[i][j] == '\\': return newGrid[i][j][1] # Bottom
    else: return newGrid[i][j][0] # Top

  # Connect graph
  for i in range(n):
    for j in range(n):
      square = grid[i][j]
      if square == ' ':
        if goLeft(i, j): newGrid[i][j][0].next.append(goLeft(i, j))
        if goRight(i, j): newGrid[i][j][0].next.append(goRight(i, j))
        if goUp(i, j): newGrid[i][j][0].next.append(goUp(i, j))
        if goDown(i, j): newGrid[i][j][0].next.append(goDown(i, j))
      elif square == '\\':
        if goLeft(i, j): newGrid[i][j][1].next.append(goLeft(i, j))
        if goRight(i, j): newGrid[i][j][0].next.append(goRight(i, j))
        if goUp(i, j): newGrid[i][j][0].next.append(goUp(i, j))
        if goDown(i, j): newGrid[i][j][1].next.append(goDown(i, j))
      elif square == '/':
        if goLeft(i, j): newGrid[i][j][0].next.append(goLeft(i, j))
        if goRight(i, j): newGrid[i][j][1].next.append(goRight(i, j))
        if goUp(i, j): newGrid[i][j][0].next.append(goUp(i, j))
        if goDown(i, j): newGrid[i][j][1].next.append(goDown(i, j))
  
  # Now dfs
  visited = set()

  def dfs(currNode):
    if currNode in visited: return
    visited.add(currNode)

    for node in currNode.next:
      dfs(node)
  
  numIslands = 0
  for i in range(n):
    for j in range(n):
      for k in range(len(newGrid[i][j])):
        if newGrid[i][j][k] not in visited:
          numIslands += 1
          dfs(newGrid[i][j][k])
    
  return numIslands

# print(solve([" /","/ "]))