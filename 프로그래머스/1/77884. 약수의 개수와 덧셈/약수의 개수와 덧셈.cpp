#include <cmath>

using namespace std;

// 1. left 부터 right까지 탐색
// 2. 루트 i가 정수일 때만 약수의 개수가 홀수

int solution(int left, int right) {
    int answer = 0;
    
    for(int i = left; i <= right; i++){  
        if(sqrt(i) == (int)sqrt(i)) answer -= i;
        else answer += i;
    }
    
    return answer;
}