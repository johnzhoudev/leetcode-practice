"""

371. Sum of Two Integers

no using + and -

do old fashioned way with bits

Tactic: Do xor (simulates adding without carry), and other number is the carry (a & b) << 1. Then keep adding while 2nd number != 0. Use c++!

"""
class Solution {
public:
    int getSum(int a, int b) {
        int c;
        while (b != 0) {
            c = a ^ b;
            b = ((a & b) << 1);
            a = c;
        }
        return a;
    }
};

// def solve(a, b):

//     while b != 0:
//         tmpa = a
//         a = a ^ b # xor
//         b = (tmpa & b) << 1 # carries

//     return a

// def solve(a, b):
//     carry = 0
//     sum = 0
//     curr_bit = 1
//     while a or b:
//         if a & 1 and b & 1 and carry:
//             sum |= curr_bit
//             carry = 1
//         elif carry:
//             if (a & 1 or b & 1): # Cannot both be true
//                 carry = 1
//             else:
//                 sum |= curr_bit
//                 carry = 0 # apply carry
//         elif a & 1 and b & 1: # no carry, both active
//             carry = 1
//         elif a & 1 or b & 1: # one of them, carry must be none
//             assert carry == 0
//             sum |= curr_bit
        
//         # else none
//         curr_bit <<= 1
//         a >>= 1
//         b >>= 1
    
//     if carry:
//         sum |= curr_bit

//     return sum

// # print(solve(2, 3))
// print(bin(-1))
// print(-1 & 1)
           
