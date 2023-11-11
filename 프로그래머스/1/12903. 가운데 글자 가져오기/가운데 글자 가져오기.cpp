#include <cstring>
#include <iostream>
#include <vector>

using namespace std;

string solution(string s) {
    int idx = s.length() / 2;                   // 중간 index
    if(s.length() % 2) return s.substr(idx, 1); // 홀수면 가운데 반환
    else return s.substr(idx - 1, 2);           // 짝수면 2글자 반환
}