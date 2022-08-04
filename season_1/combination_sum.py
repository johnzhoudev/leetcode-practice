"""
Combination sum

array of distinct integers
target
Return list of all unique combinations of where chosen nums sum to target.
- can return combinations in any order
- nums chosen with replacement (unlimited times)
- combinations unique if frequency of at least 1 num is different
- guaranteed num unique combos is < 150 - hardcoded stop here?
candidates.length <= 30
1 <= int <= 200 (all positive)
1 <= target <= 500 -> 500 items in the map

Ideas:
- Brute force?: iterate thru all combinations, check which ones reach target
	- how to iterate thru all combinations?
	- If you can iterate thru each combo O(1), O(n!) n choose r is O(n! * n)

- Big hashmap: Same idea as 3sum, but map[num] = list of combos that sum to num
	- how to generate all combos?
	- go 1 item at a time, and add repeatedly to each unique combo as long as it's under target.
	- also since we always add new numbers at new freq, will not duplicate combinations. Like adding in sorted order
	- Proof: consider a combo that sums to target. order the numbers in added order. will have to be added!
	- n = num items in candidates, m = max num times an int can be summed up to get target
	- Runtime: O(n * m + n!)
	- space: O()

Any better?
- 

"""