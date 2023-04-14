/*


https://leetcode.com/problems/interleaving-string/

- is s3 an interleaving of substrings of s1 and s2?

Ideas:

- Try with s1, match beginning.
- then subproblem is can you interleave rest with s2, and rest of s1

States: rest of s3, rest of s1, rest of s2, who's interleaving
- search alg to do this, plus memoization

O(l1 * l2 * l3)

- If l1 and l2 can subleave. Don't need to keep track of turn.

Tactic: state[i][j] = if s1[:i] and s2[:j] can subleave to s3[:i+j]. Don't have to worry abt turn, since all valid. 2x in row means once. cases, add 1 char at a time.


*/

class Solution {
public:


    bool isInterleave(string s1, string s2, string s3) {
        if (s1.size() + s2.size() != s3.size()) {
            return false;
        }

        bool state[s1.size() + 1][s2.size() + 1];
        state[0][0] = true;

        for (int i = 0; i <= s1.size(); i++) {
            for (int j = 0; j <= s2.size(); j++) {
                if (i == 0 && j == 0) {
                    continue;
                } else if (i == 0) {
                    // use j 
                    state[i][j] = (state[i][j-1] && s2[j-1] == s3[i + j - 1]);
                } else if (j == 0) {
                    state[i][j] = (state[i-1][j] && s1[i-1] == s3[i + j - 1]);
                } else {
                    state[i][j] = (state[i][j-1] && s2[j-1] == s3[i + j - 1]) || (state[i-1][j] && s1[i-1] == s3[i + j - 1]);
                }
            }
        }

        return state[s1.size()][s2.size()];
    }

};

    // bool dfs(string &s1, string &s2, string &s3, Data currState, set<Data> &state) {
    //     // check base case
    //     if (currState.s1 == s1.size() && currState.s2 == s2.size() && currState.s3 == s3.size()) {
    //         return true;
    //     } else if (currState.s1 >= s1.size() || currState.s2 >= s2.size() || currState.s3 >= s3.size()) {
    //         return false; // didn't manage to match
    //     }

    //     // Check state
    //     if (state.find(currState))

    //     // all in valid ranges, so expand. 
    //     int i = currState.s1;
    //     int s = currState.s3;
    //     while (true) {
    //         if (s1[i] == s3[s]) {
    //             // do dfs and advance, since matches
    //             if (dfs(s2, s1, s3, Data(i+1, currState.s2, s), state)) {
    //                 return true;
    //             }
    //             i++;
    //             s++;
    //         } else {
    //             break;
    //         }
    //     }


// struct Data {
//     int s1;
//     int s2;
//     int s3;
//     bool isFirst;
//     Data(int a, int b, int c): s1{a}, s2{b}, s3{c} { }
// };




    // }