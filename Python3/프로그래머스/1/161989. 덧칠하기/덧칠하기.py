def solution(n, m, section):
    answer, y = 0, section[0] - 1
    
    for s in section:
        if s < y:
            continue
        y = s + m
        answer += 1
            
    return answer