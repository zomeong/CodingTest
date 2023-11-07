#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <queue>
#define MAX 110
#define FIO ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
using namespace std;

vector<int> adj[MAX];

int bfs(int n1, int n2) {
	queue <int> q;
	bool visited[MAX] = { 0, };
	memset(visited, false, sizeof(visited));
	int nodeCnt = 1;

	q.push(n1);
	visited[n1] = true;
	visited[n2] = true;

	while (!q.empty()) {
		int node = q.front();
		q.pop();

		for (int i = 0; i < adj[node].size(); i++) {
			int next = adj[node][i];

			if (!visited[next]) {
				nodeCnt++;
				visited[next] = 1;
				q.push(next);
			}
		}
	}

	return nodeCnt;
}

int solution(int n, vector<vector<int>> wires) {
	int answer = MAX;
	vector <int> node;

	if (n == 2) return 0;

	for (int i = 0; i < wires.size(); i++) {
		adj[wires[i][0]].push_back(wires[i][1]);
		adj[wires[i][1]].push_back(wires[i][0]);
	}

	int g_size = bfs(1, 1);

	for (int i = 0; i < wires.size(); i++) {
		int cnt = bfs(wires[i][0], wires[i][1]);
		answer = min(answer, abs(2 * cnt - n));
	}

	return answer;
}