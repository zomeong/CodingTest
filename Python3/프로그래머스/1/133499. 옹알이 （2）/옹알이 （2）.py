def solution(babbling):
    answer = 0
    pron = ["aya", "ye", "woo", "ma"]
    
    for p in pron:
        babbling = [b.replace(p*2, '1') for b in babbling]
        babbling = [b.replace(p, '2') for b in babbling]
    
    for b in babbling:
        if all(char == '2' for char in b):
            answer += 1
    
    return answer
    