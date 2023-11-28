#include <string>
#include <vector>
#include <iostream>
#include <map>
using namespace std;

// 1. 현재 위치에서 바로 다음 글자를 더한 문자열을 저장
// 2. 사전에서 가장 긴 문자열 w를 찾음
// 3. 사전에 w+c 저장
// 3-1. 길이가 1일 경우 아스키코드로 계산하여 출력
// 3-2. 사전은 map으로 설정하여 key값에 27과 현재 사전크기를 더한 값 저장
// 4. 색인번호 저장

map<string, int> dic;

vector<int> solution(string msg) {
    vector<int> answer;

    int p = 0;
    int len = msg.length();
    for(int i = 0; i < len; i++) {
        if (i == len - 1) {
            answer.push_back((char)msg[i] - 64);
            break;
        }

        string str = msg.substr(i, 2);

        while (true) {
            if (dic.find(str) != dic.end()) {
                i += 2;
                if (i > len) break;
                str += msg[i--];
            }
            else break;
        }

        dic[str] = dic.size() + 27;
        if(str.length() == 2) answer.push_back((char)msg[i] - 64);
        else {
            str.erase(str.size() - 1);
            answer.push_back(dic[str]);
        }
    }

    return answer;
}