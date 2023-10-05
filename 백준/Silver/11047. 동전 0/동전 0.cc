#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#define MAX 11
#define FIO ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
using namespace std;

int main() {
	FIO;
	
	int n, k, cnt = 0;
	int worth[MAX];
	cin >> n >> k;

	for (int i = 0; i < n; i++)
		cin >> worth[i];
	
	for (int i = n - 1; i >= 0; i--) {
		if (worth[i] <= k) {
			k = k - worth[i];
			cnt++;
			i++;
		}
		if (k == 0) break;
	}

	cout << cnt;
}