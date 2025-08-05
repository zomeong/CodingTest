from collections import Counter

def solution(X, Y):
    answer = ''
    
    # 문자열의 문자 요소 카운트
    x_count = Counter(X)
    y_count = Counter(Y)
    
    # 교집합 = 공통 정수 카운트 딕셔너리
    union = x_count & y_count
    
    # 내림차순 정렬
    reunion = sorted(union.items(), key = lambda x:int(x[0]), reverse=True)
    
    if len(reunion) == 0:
        return "-1"
    
    for u in reunion:
        answer += u[0] * u[1]
        
    if answer[0] == '0':
        answer = "0"
    
    return answer