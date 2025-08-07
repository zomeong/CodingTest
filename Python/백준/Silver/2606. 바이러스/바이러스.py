from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    result = 0

    while queue:
        v = queue.popleft()
        for g in graph[v]:
            if not visited[g]:
                queue.append(g)
                visited[g] = True
                result += 1

    return result

def main():

    n, m = int(input()), int(input())
    graph = [[] for i in range(n + 1)]
    visited = [False for i in range(n + 1)]
    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    result = bfs(graph, 1, visited)
    print(result)

    return

if __name__ == "__main__":
    main()