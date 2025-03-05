def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        answer += -i if i ** 0.5 == (int)(i ** 0.5) else i
    return answer