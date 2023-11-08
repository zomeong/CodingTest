#include <iostream>
using namespace std;

int n, m;
int arr[10];
bool visited[10];

void go(int index, int pre) {
	if (index == m) {
		for (int i = 0; i < m; i++)
			printf("%d ", arr[i]);
		printf("\n");
		return;
	}

	for (int i = pre; i <= n; i++) {
		arr[index] = i;
		pre = i;
		go(index + 1, pre);
		arr[index] = 0;
	}
	return;
}

int main()
{
	scanf("%d %d", &n, &m);

	go(0, 1);

	return 0;
}