#include <vector>

using namespace std;

vector<int> solution(int n, long long left, long long right) {
    vector<int> answer;
    
    int x = left / n + 1;
    int y = left % n + 1;

    while(1) {
        for (int i = y; i <= n; i++) {
            if (i <= x) answer.push_back(x);
            else answer.push_back(i);

            if (answer.size() == right - left + 1) return answer;
        }
        x++;
        y = 1;
    }
}
