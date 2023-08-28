"""


2 sorted arrays
merge
dixie cup

must store results in array 1
can i do it in O(1) space?
- swap elements when doing
x doesn't work.  starves array 2

Better, go backwards, and use end space in array 1 to compare and decrement

Tactic: Go backwards for O(1) space, and paste directly in. Careful, if going backwards, want to paste the larger

"""

def solve(num1, m, num2, n):
    i = m-1
    k = n-1 
    curr = m + n - 1

    while curr >= 0:
        print(num1)

        if k < 0: break
        if i < 0:
            # copy all of k
            while k >= 0:
                num1[curr] = num2[k]
                k -= 1
                curr -= 1
            break

        if num1[i] >= num2[k]:
            num1[curr] = num1[i]
            i -= 1
        else:
            num1[curr] = num2[k]
            k -= 1

        curr -= 1
    
