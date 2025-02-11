from itertools import combinations

def solution(number):
    
    answer = 0
    results = list(combinations(number, 3))
    
    for result in results:
        if sum(result) == 0:
            answer += 1
    return answer