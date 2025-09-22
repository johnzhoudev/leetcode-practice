"""

91. Decode Ways

numbers, figure out letters map? ways?

26 in total

do dfs, take 1 vs take 2
O(num solns)

dp? num ways to break number?

1 digit + last or 2 digits plus 2 last
O(n)

dp[i] = number of ways to decode dp[i-1] (if possible), or dp[i-1] (if possible, double)

"""

def solve(s):
    dp = [0 for _ in range(len(s))]

    # Edge case
    if s[0] == '0':
        return 0
    elif len(s) == 1:
        return 1
    
    # helper func
    def num_ways(str):
        if len(str) == 1 and str == '0':
            return 0
        elif len(str) == 2 and str[0] == '0':
            return 0
        
        # At this point, either single non-zero digit, or 2 digit, first can't be 0
        if len(str) == 1:
            return 1

        
        num_left = num_ways(str[0])
        num_right = num_ways(str[1])

        # if no way on right, must be 1 way
        if num_right == 0:
            return 1

        # Can potentially combine
        # Splitting in 2 is only 1 way
        return num_left + (1 if int(str) <= 26 else 0)
    
    def is_valid(str):
        if len(str) == 1 and str == '0':
            return 0 # invalid
        elif len(str) == 2 and str[0] == '0':
            return 0 # invalid
        # At this point, either single non-zero digit, or 2 digit, first can't be 0
        return 1 if int(str) <= 26 else 0
        
    # assert is_valid('0') == 0
    # assert is_valid("01") == 0
    # assert is_valid("10") == 1
    # assert is_valid("20") == 1
    # assert is_valid("26") == 1
    # assert is_valid('3') == 1
    # assert is_valid('27') == 0
    # assert is_valid('16') == 1
    # Test cases
    # assert num_ways('0') == 0
    # assert num_ways("01") == 0
    # assert num_ways("10") == 1
    # assert num_ways("20") == 1
    # assert num_ways("26") == 3
    # assert num_ways('3') == 1
    # assert num_ways('27') == 2
    # assert num_ways('16') == 3

    # Base cases
    dp[0] = 1 # 1st digit must be valid number
    dp[1] = is_valid(s[0] + s[1]) + dp[0] * is_valid(s[1])

    for i in range(2, len(s)):
        dp[i] = dp[i-1] * is_valid(s[i]) + dp[i-2] * is_valid(s[i-1] + s[i])
    
    # print(dp)
    return dp[-1]

print(int("01"))
print(solve("301"))