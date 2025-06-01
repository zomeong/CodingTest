def solution(a, b):
    day = ["THU", "FRI","SAT","SUN","MON","TUE","WED"]
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    d = b + sum(month[0:a - 1])
    answer = day[d % 7]
    
    return answer