#include <string>
#include <vector>

using namespace std;

vector<double> solution(int k, vector<vector<int>> ranges) {
    vector<double> answer;
    vector<double> y;
    vector<double> area;

    // 우박 수열
    y.push_back(k);
    while (k != 1) {
        if (k % 2) k = k * 3 + 1;
        else k /= 2;

        y.push_back(k);
    }
    int n = y.size();

    // 구간 넓이
    for (int i = 0; i < n - 1; i++) {
        double a = (y[i] + y[i + 1]) / 2;
        area.push_back(a);
    }

    for (int i = 0; i < ranges.size(); i++) {
        if (ranges[i][0] >= n + ranges[i][1]) {
            answer.push_back(-1);
            continue;
        }

        double sum = 0;
        for (int j = ranges[i][0]; j < n + ranges[i][1] - 1; j++) {
            sum += area[j];
        }
        answer.push_back(sum);
    }

    return answer;
}