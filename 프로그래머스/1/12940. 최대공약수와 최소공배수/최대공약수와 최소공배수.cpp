#include <vector>
#include <utility>

using namespace std;

vector<int> solution(int n, int m) {
    vector<int> answer;
    if(n > m) swap(n, m);
    
    for(int i = n; i > 0; i--){
        if(n % i == 0 && m % i == 0){
            answer.push_back(i);
            break;
        }
    }
    
    for(int i = 1; i <= n; i++){
        int t = m * i;
        if(t % n == 0) {
            answer.push_back(t);
            break;
        }
    }
    
    return answer;
}