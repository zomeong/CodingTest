#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

string solution(string s) {
    string answer = "";
    vector<int> num;
    istringstream iss(s);

    while(iss) {
        string token;
        iss >> token;
        if(!token.empty()) num.push_back(stoi(token));
    }

    sort(num.begin(), num.end());

    answer += to_string(num.front()) + " ";
    answer += to_string(num.back());

    return answer;
}