#include <string>
#include <vector>

using namespace std;

bool solution(string s) {
    bool answer = true;
    
    if(s.size() != 4 && s.size() != 6) return false;
    
    for(int i = 0; i < s.size(); i++){
        int asc = s[i] - 0;
        if(asc > 57 || asc < 48) return false;
    }
    
    return answer;
}