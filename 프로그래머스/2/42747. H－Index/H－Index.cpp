#include <vector>
#include <algorithm>

using namespace std;

// 1. 벡터 내림차순 정렬
// 2. answer 0부터 1씩 증가하며 벡터 탐색
// 3. i가 인용횟수보다 작으면 answer++

int solution(vector<int> citations) {

    sort(citations.begin(), citations.end(), greater<int>());

    int s = citations.size();

    int answer = 0;
    if (!citations[0]) return 0;
    if (citations[s - 1] >= s) return s;

    for (int i = 0; i < s; i++) {
        if (citations[i] > i) answer++;
        else break;
    }

    return answer;
}