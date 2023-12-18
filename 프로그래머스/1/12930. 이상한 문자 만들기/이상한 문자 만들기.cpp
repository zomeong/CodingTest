#include <string>
#include <vector>
#include <cctype>

using namespace std;

string solution(string s) {
    string answer = "";
    
    int i = 0;
    for(char c : s){
        if(c == ' '){
            answer.push_back(c);
            i = 0;
            continue;
        }
        
        if(i % 2) c = tolower(c);
        else c = toupper(c);
        answer.push_back(c);
        i++;
    }
    
    return answer;
}