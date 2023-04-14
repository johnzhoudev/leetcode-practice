// Tactic: Classic DP, just t/f for each part. Careful for base cases

#include <vector>

using namespace std;

class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> s(m, vector<int>(n, 1));

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                s[i][j] = s[i-1][j] + s[i][j-1];
            }
        }

        return s[m-1][n-1];
    }
};

class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> s;
        for (int i = 0; i < m; i++) {
            vector<int> fogRow;
            for (int j = 0; j < n; j++) {
                fogRow.push_back(0);
            }
            s.push_back(fogRow);
        }
        // Base cases
        for (int j = 0; j < n; j++) {
            s[0][j] = 1;
        }
        for (int i = 0; i < m; i++) {
            s[i][0] = 1;
        }

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                s[i][j] = s[i-1][j] + s[i][j-1];
            }
        }

        return s[m-1][n-1];
    }
};