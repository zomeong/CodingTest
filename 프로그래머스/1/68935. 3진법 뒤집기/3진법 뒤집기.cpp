#include <string>
#include <cmath>

using namespace std;

int solution(int n) {
    int answer = 0;
    string three;
    
    while(n > 0){
        three += to_string(n % 3);
        n /= 3;
    }
    
    int len = three.length() - 1;
    for(int i = len; i >= 0 ; i--){
        answer += (three[i] - '0') * pow(3, len - i);
    }
     
    return answer;
}