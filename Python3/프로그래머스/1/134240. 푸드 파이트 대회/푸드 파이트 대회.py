def solution(food):
    answer = ''
    
    for i in range(len(food)):
        answer += (food[i] // 2) * str(i)
    
    answer += "0" + answer[::-1]
    return answer 