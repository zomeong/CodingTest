#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(vector<int> a, vector<int> b, int col) {
    if (a[col] == b[col]) return a[0] > b[0];
    return a[col] < b[col];
}

int solution(vector<vector<int>> data, int col, int row_begin, int row_end) {
    int answer = 0;
    vector <int> si;
    col--;

    sort(data.begin(), data.end(), [col](const auto& a, const auto& b) {
        return compare(a, b, col);
        });

    for (int i = row_begin - 1; i < row_end; i++) {
        int s = 0;

        for (int j = 0; j < data[i].size(); j++) {
            s += data[i][j] % (i + 1);
        }

        si.push_back(s);
    }

    for (int i : si) {
        answer ^= i;
    }

    return answer;
}