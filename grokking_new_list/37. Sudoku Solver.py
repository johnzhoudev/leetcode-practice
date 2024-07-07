"""
https://leetcode.com/problems/sudoku-solver/

37. Sudoku Solver

given board, solve sudoku...
guaranteed only 1 solution

Search algorithm?
- keep viable options data for each row, col and square
- each time you add a value, mark off for row, col and square

- most constrained variable
- least constraining value


search algorithm for each square, for each number
- iterative? try recursive for now
- store state as square to pick, and numbers used

Tactic: Use sets to store numbers in rows / cols and to check if valid, and just loop thru all choices and undo if necessary.
- Tip just check rows cols and square manually for isvalid check to avoid storing sets
"""

def solve(board):
  rows = [set() for _ in range(9)]
  cols = [set() for _ in range(9)]
  squares = [[set() for _ in range(3)] for _ in range(3)]

  def getSquareSet(row, col):
    return squares[row // 3][col // 3]
  
  def getSets(row, col):
    return rows[row], cols[col], getSquareSet(row, col)

  def isValid(row, col, value): # checks if adding this value would be valid
    rowVals, colVals, squareVals = getSets(row, col)
    return value not in rowVals and value not in colVals and value not in squareVals
  
  def setup():
    for i in range(len(board)):
      for j in range(len(board)):
        if board[i][j] != ".":
          num = int(board[i][j])
          rows[i].add(num)
          cols[j].add(num)
          getSquareSet(i, j).add(num)
  setup()
  # print(rows)
  # print(cols)
  # print(squares)

  solved = False

  def getNext(row, col):
    if col != 8:
      return row, col + 1
    return row + 1, 0

  def dfsNext(row, col):
    nRow, nCol = getNext(row, col)
    dfs(nRow, nCol)
    
  def dfs(row, col):
    # Checking at this point

    # Check Solved
    # print(board)
    # print(rows)
    # print(cols)
    # print(squares)

    if (row >= 9 or col >= 9):
      nonlocal solved
      solved = True
      return

    if board[row][col] != ".":
      dfsNext(row, col)
      return

    for val in range(1, 10):
      if isValid(row, col, val):
        rows[row].add(val)
        cols[col].add(val)
        getSquareSet(row, col).add(val)
        board[row][col] = str(val)

        # Try
        dfsNext(row, col)

        if solved:
          return

        # remove old 
        board[row][col] = "."
        rows[row].remove(val)
        cols[col].remove(val)
        getSquareSet(row, col).remove(val)

  dfs(0, 0)
  return board
    
print(solve([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
# print(solve([[".",".","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]))