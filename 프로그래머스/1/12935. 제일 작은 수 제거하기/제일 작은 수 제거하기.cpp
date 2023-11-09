#include <algorithm>
#include <vector>

using namespace std;


vector<int> solution(vector<int> v) {
    int min_ele = *min_element(v.begin(), v.end());
    v.erase(remove(v.begin(), v.end(), min_ele), v.end());
    
    if(v.empty()) v.push_back(-1);
    
    return v;
}