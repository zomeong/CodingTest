#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

string numbers;
vector <int> num;
vector <int> v;

// 모든 조합 구하기
void makeNums(int len) {
	for (int j = 1; j <= len; j++) {
		do {
			int n = 0;
			for (int i = 0; i < j; i++)
				n += pow(10, j - i - 1) * num[i];		
			v.push_back(n);

		} while (next_permutation(num.begin(), num.end()));
	}
}

// 소수인지 판별
bool isPrime(int n) {
	if (n <= 1) return false;

    // 2부터 루트 n까지 순회
	for (int i = 2; i * i <= n; i++) {	
        // 나누어 떨어지면 소수가 아님
		if (n % i == 0) return false;	
	}

	return true;
}

int solution(string numbers) {
    int answer = 0;
    
    int len = numbers.length();

    // 문자열을 순회하며 숫자 하나씩 벡터에 넣음
	for (int i = 0; i < len; i++) 
		num.push_back(numbers[i] - '0');		
	sort(num.begin(), num.end());
	makeNums(len);						

    // 중복 제거
	sort(v.begin(), v.end());
	v.erase(unique(v.begin(), v.end()), v.end());	

	for (int i = 0; i < v.size(); i++)
		if (isPrime(v[i])) answer++;	
    
    return answer;
}