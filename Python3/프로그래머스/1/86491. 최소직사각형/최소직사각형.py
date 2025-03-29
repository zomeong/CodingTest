def solution(sizes):
    answer = [0, 0]
    
    for s in sizes:
        if s[0] < s[1]:
            s[0], s[1] = s[1], s[0]
            
        answer[0] = max(s[0], answer[0])
        answer[1] = max(s[1], answer[1])
    
    return answer[0] * answer[1]