#include <iostream>
#include <string>
#include <queue>
#include <stack>

using namespace std;

string b = "[](){}";

bool check(queue <char> q) {
    stack <char> st;
    
    while(!q.empty()) {
        char f = q.front();
        q.pop();

        if (f == '[' || f == '{' || f == '(') st.push(f);
        else {
            if (st.empty()) return false;

            size_t loc = b.find(f);
            if (b[loc - 1] == st.top()) st.pop();
            else return false;
        }
    }
    return st.empty();
}

int solution(string s) {
    int answer = 0;
    queue <char> q;

    for (int i = 0; i < s.length(); i++) {
        q.push(s[i]);
    }

    for (int i = 0; i < q.size() - 1; i++) {
        if (check(q)) answer++;

        char f = q.front();
        q.pop();
        q.push(f);
    }

    return answer;
}