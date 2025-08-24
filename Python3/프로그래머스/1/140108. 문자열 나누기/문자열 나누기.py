def solution(s):
    answer = 0
    x = s[0]
    x_cnt = 0
    cnt = 0
    l = len(s)
    
    for c in s:
        if x_cnt == 0:
            x = c
        
        if c == x:
            x_cnt += 1
        else:
            cnt += 1
            
        if x_cnt == cnt:
            answer += 1
            x_cnt = 0
            cnt = 0
            
            
    if x_cnt != 0 or cnt != 0:
        answer += 1
    
    return answer