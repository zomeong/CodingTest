def solution(t, p):
    answer, pl = 0, len(p)
    
    for i in range(len(t) - pl + 1):
        if int(t[i:i + pl]) <= int(p):
            answer += 1
    
    return answer