def solution(n):
    t, answer, cnt = '', 0, 0
    
    while n > 0:
        t += str(n % 3)
        n //= 3
        
    for i in reversed(t):
        answer += int(i) * (3 ** cnt)
        cnt += 1
        
    return answer
        