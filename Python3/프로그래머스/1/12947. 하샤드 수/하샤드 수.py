def solution(x):
    answer = 0;
    
    for i in str(x):
        answer += int(i)
    
    return True if x % answer == 0 else False