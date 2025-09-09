def solution(s, skip, index):
    answer = ''
    alpa = "abcdefghijklmnopqrstuvwxyz"
    length = 26 - len(skip)
    
    for sk in skip:
        alpa = alpa.replace(sk, "")
    
    for c in s:
        f = alpa.find(c)
        idx = (f + index) % length
        answer += alpa[idx]
    
    return answer