def solution(a, b):
    day = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    
    date = b + sum(month[0:a - 1])
    
    return day[date % 7]