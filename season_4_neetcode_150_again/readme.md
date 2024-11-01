# Neetcode 150 Tips

Leetcode Progression Ideas:

- Neetcode 150, finish by end of august - 3-4 q a day
    - Notes on common tactics for each part and example questions
- Grokking finish list randomly - 3q a day?
- Neetcode All, do randomly - 3 q a day?

# Tactics

## Intervals
- Finding number of days / rooms needed for intervals, sort by end and greedy, append to largest possible endtime - Meeting Schedule II
- Inserting interval, collect left and right and overlap min max - 57. Insert Interval
- Merging Intervals - sort and add, if overlapping then min max merge with last. - 56. Merge Intervals 
- Removing until non overlapping - Greedily take with earliest end - 435. Non-overlapping intervals
- HARD: Intervals and queries - 1851 Minimum interval to include each query

## Backtracking
- General backtracing with subsets - 39. Combination sum, 78 Subsets, 46 permutations
- Subsets backtracing with duplicates, use idx and count - or either add, or advance to next non dupe. - 90 subsets ii, 40. combination sum 2
- Grid backtracking - 79. word search
- Palindrome partitioning - try to see if prefix is palindrome, and recurse on remaining.
- N Queens grid backtracking, advance row and use y intercept to track diagonals

## Basic Graphs
- DFS - number of islands 200 / max area of island 695
- DFS Clone Graph - 133 Clone Graph
- BFS from multiple points with cool bfs for size trick - Walls and Gates, 994. Rotting Oranges
- DFS / BFS from ocean - 417. Pacific Atlantic Water Flow, surrounded regions 130
- Topological Sort with DFS / indegrees - 207 Course Schedule, 210 Course Schedule 2
- Cycle detection in undirected graph / remove back edge - Graph Valid tree
- Union Find with Rank and Collapse - Redundant Connection
- WordLadder wildcard tactic!!! - 127

## Advanced Graphs
- Eulerian Path Alg! - 332
- Prim vs Kruskal alg for finding Min Spanning Tree - 1584
- Dijkstra's alg - min path to all dests - 743
- Topological sort with DFS or indegrees - Alien dictionary
- bfs iterative? - 787 cheapest flights within k stops

## 1D DP
- Classic DP - 198 house robber, 746 Min cost climbing stairs
- House Robber circular - do 2 solves, 1 with first removed and 1 with last removed - 213
- Longest Palindromic Substring - Not even DP, check palindromes from middle - 5
- *** Decode Ways - if 1-9, add dp[i-1]. If 10-26, add dp[i-2]. If nothing added, return 0. TRICKY!
- Knapsack problem - 322 Coin Change 
- Maximum product subarray - keep max and min values in dp - 152 Maximum Product Subarray
- Check if string can be made of words - 139 Word Break
- 01 Knapsack, or expanding set of reachable sums - 416 Partition Equal Subset Sum

## 2D DP
- Longest Common Subsequence - build up, use or not use - 1143, 115. distinct subsequences
- DFS with memoization / state machine - Best time to buy or sell stock with cooldown 309
- knapsack with unlimited coins - coin change 2 518
- DFS with Memoization for Knapsack like question - 494 Target Sum
- interleaving string - dfs with memoization - 97 interleaving string, 329 longest path in matrix
- Burst Balloons - Interval DP but pivot is the LAST item removed, account for left and right edges - 312 Burst Balloons
- Kleene Star regex handling - 10 Reg Exp Matching

## Greedy
- Maximum Subarray greedy, take total + curr or just curr
- Jump game just expand highest
- Gas stations - total gas - cost >= 0 => solution! 134
- Hand of straights - hashes and sorting
- Merge triplets - don't need to sort! Just filter out anything with higher values

## Arrays and Hashing
- Encoding and Decoding strings utf-8 - add char count and # prefix


Cheat Sheet: https://docs.google.com/spreadsheets/d/1LaQWNzYnkYukygLMTQt7lBV11lc1F30hTDcCrjswn-U/edit?gid=0#gid=0