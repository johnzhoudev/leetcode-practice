# Results:
# Runtime: 244ms 64.76%
# Memory Usage: 25.7MB 5.64%

"""

https://leetcode.com/problems/product-of-array-except-self

int array nums
return array
answer[i] is product of all nums except nums[i]

Idea:
O(n), multiply all, then just divide by nums i?
O(n) space?
No Division! But still O(n)

Edge case: num is 0

Ideas:
- have solutions for prefix and suffix multiples, and multiply them
- O(n) to generate each one, and O(1) to combine, plus no divisions

Tactic: Use prefix and postfix arrays. Also, can do in place in result array
"""

def solve(nums):
    result = [1 for _ in range(len(nums))]
    pre = 1
    for idx, num in enumerate(nums):
        result[idx] = pre * num
        pre *= num
    
    post = 1
    for idx, num in reversed(list(enumerate(nums))):
        if idx == 0:
            result[idx] = post
            continue
        result[idx] = result[idx - 1] * post
        post *= num
    return result




def solve(nums):
    prefixes = []
    for num in nums:
        if len(prefixes) == 0:
            prefixes += [num]
        else:
            prefixes += [prefixes[-1] * num]
    
    suffixes = []
    for num in reversed(nums): # indices away from right
        if len(suffixes) == 0:
            suffixes += [num]
        else:
            suffixes += [suffixes[-1] * num]
    
    answer = [suffixes[len(nums) - 2]]
    for i in range(1, len(nums) - 1): # inner
        answer += [prefixes[i - 1] * suffixes[len(nums) - i - 2]]
    answer += [prefixes[len(nums) - 2]]

    return answer


