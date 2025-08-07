#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

bool visited_d[110];
bool visited_b[110];
vector <int> adj[110];
queue <int> q;

int cnt = -1;

void bfs(int st) {
    visited_b[st] = 1;
    q.push(st);

    while (!q.empty()) {
        int now = q.front();
        q.pop();
        cnt++;

        for (int i = 0; i < adj[now].size(); i++) {
            int next = adj[now][i];
            if (!visited_b[next]) {
                visited_b[next] = 1;
                q.push(next);
            }
        }
    }
}

int main()
{
    int n, m, x, y;
    scanf("%d", &n);
    scanf("%d", &m);

    for (int i = 0; i < m; i++) {
        scanf("%d %d", &x, &y);
        adj[x].push_back(y);
        adj[y].push_back(x);
    }
        
    for (int i = 0; i <= n; i++)
        sort(adj[i].begin(), adj[i].end());
    
    bfs(1);
    printf("%d", cnt);

    return 0;
}