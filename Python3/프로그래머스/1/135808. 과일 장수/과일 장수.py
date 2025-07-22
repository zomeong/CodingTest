def solution(k, m, score):
    score.sort(reverse=True)
    
    i,answer = m - 1, 0
    while i < len(score):
        answer += score[i] * m
        i += m
        
    return answer