def solution(babbling):
    answer = 0
    pron = ["aya", "ye", "woo", "ma"]
    pron2 = ["ayaaya", "yeye", "woowoo", "mama"]
    
    for p2 in pron2:
        babbling = [b.replace(p2, '1') for b in babbling]
    
    for p in pron:
        babbling = [b.replace(p, '2') for b in babbling]
    
    for b in babbling:
        if all(char == '2' for char in b):
            answer += 1
    
    return answer
    