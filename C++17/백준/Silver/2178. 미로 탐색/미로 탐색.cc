#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int visited[105][105];
int dx[4] = { 1, -1, 0, 0 };
int dy[4] = { 0, 0, -1, 1 };
queue <pair <int, int>> q;
string a[105];
int n, m;

void bfs(int i, int j) {
    visited[i][j] = 1;
    q.push(make_pair(i, j));

    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for (int k = 0; k < 4; k++){
            int nextx = x + dx[k];
            int nexty = y + dy[k];

            if (nextx >= 0 && nextx < n && nexty >= 0 && nexty < m && a[nextx][nexty] == '1' && !visited[nextx][nexty]) {
                visited[nextx][nexty] = visited[x][y] + 1;
                q.push(make_pair(nextx, nexty));
            }
        }
    }
}

int main()
{
    scanf("%d %d", &n, &m);

    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
  
    bfs(0, 0);
    printf("%d", visited[n - 1][m - 1]);

    return 0;
}