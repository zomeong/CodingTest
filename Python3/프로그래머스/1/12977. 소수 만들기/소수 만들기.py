from itertools import combinations

def solution(nums):
    answer = 0
    result = list(combinations(nums, 3))
    
    for r in result:
        if check(sum(r)):
            answer += 1
    
    return answer

def check(n):
    for i in range(2, round(n ** 0.5 + 1)):
        if n % i == 0:
            return False 
    return True