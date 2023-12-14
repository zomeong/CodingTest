#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

// 1. 문자열을 2차원 벡터로 파싱
// 2. 원소 벡터의 크기에 따라 정렬
// 3. 벡터를 순회하며 answer 벡터에 없으면 원소 추가

bool compare(const vector<int>& v1, const vector<int>& v2) {
    return v1.size() < v2.size();
}

vector<int> solution(string s) {
    vector<int> answer;
    vector<vector <int>> v;

    vector <int> now;
    string num;
    for (int i = 0; i < s.length() - 1; i++) {

        if (isdigit(s[i])) {
            num += s[i];

            if (s[i + 1] == ',' || s[i + 1] == '}') {
                now.push_back(stoi(num));
                num = "";
            }
        }
        else if (s[i] == '}') {
            v.push_back(now);
            now.clear();
        }
    }

    sort(v.begin(), v.end(), compare);

    for (const auto& vec : v) {
        for (int element : vec) {
            if (find(answer.begin(), answer.end(), element) == answer.end()) {
                answer.push_back(element);
                break;
            }
        }  
    }

    return answer;
}