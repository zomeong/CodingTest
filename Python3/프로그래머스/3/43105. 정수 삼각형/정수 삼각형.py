def solution(triangle):
    answer = 0
    x = len(triangle)
    
    for n in range(1, x):
        y = len(triangle[n])
        
        for m in range(y):
            if m == 0:
                triangle[n][m] += triangle[n - 1][m]
            elif m == y - 1:
                triangle[n][m] += triangle[n - 1][m - 1]
            else:
                triangle[n][m] += max(triangle[n - 1][m - 1], triangle[n - 1][m])
    
    return max(triangle[x - 1])