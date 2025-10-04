def solution(ingredient):
    answer, i = 0, 0
    hamburger = [1, 2, 3, 1]
    
    while i <= len(ingredient) - 3:
        window = ingredient[i:i+4]
        
        if hamburger == window:
            answer += 1
            del ingredient[i:i+4]
            i = max(-1, i - 4)
        i += 1
    
    return answer