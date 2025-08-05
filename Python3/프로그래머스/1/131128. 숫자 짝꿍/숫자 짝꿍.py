from collections import Counter

def solution(X, Y):
    answer = ''
    x_count = Counter(X)
    y_count = Counter(Y)
    union = x_count & y_count
    reunion = sorted(union.items(), key = lambda x:int(x[0]), reverse=True)
    print(reunion)
    
    if len(reunion) == 0:
        return "-1"
    
    for u in reunion:
        answer += u[0] * u[1]
        
    if answer[0] == '0':
        answer = "0"
    
    return answer