def solution(babbling):
    answer = 0
    pron = ["aya", "ye", "woo", "ma"]
    
    for p in pron:
        babbling = [b.replace(p*2, '1') for b in babbling]
        babbling = [b.replace(p, ' ') for b in babbling]
    
    for b in babbling:
        if b.isspace():
            answer += 1
    
    return answer
    