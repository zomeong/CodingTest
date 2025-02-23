def solution(num):
    cnt = -1
    
    for i in range(0, 500):
        if num == 1:
            cnt = i
            break
        
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
    
    return cnt