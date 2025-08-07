from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")

    for g in graph[v]:
        if visited[g] == False:
            dfs(graph, g, visited)

def bfs(graph, n, start):
    visited = [False for i in range(n + 1)]
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True

def main():

    n, m, v = map(int, input().split())
    graph = [[] for i in range(n + 1)]

    for i in range(m):
        x, y  = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    for i in range(1, n + 1):
        graph[i].sort()

    vistied = [False for i in range(n + 1)]
    dfs(graph, v, vistied)
    print()
    bfs(graph, n, v)

    return

if __name__ == "__main__":
    main()