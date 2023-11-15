#include <string>
#include <cmath>
#include <vector>
#include <queue>

using namespace std;

// 1. 작업 일수를 큐에 저장
// 2. 큐 순회 -> 앞에 있는 수가 뒤에 있는 수보다 작을 때까지 count
// 3. count한 값 answer 벡터에 저장

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    queue <int> q;

    for (int i = 0; i < speeds.size(); i++) {
        double d = (double)(100 - progresses[i]) / speeds[i];
        q.push(ceil(d));
    }

    int count = 1;
    while (!q.empty()) {
        int f = q.front();
        q.pop();
        int count = 1;

        while (!q.empty() && q.front() <= f) {
            q.pop();
            count++;
        }

        answer.push_back(count);
    }

    return answer;
}