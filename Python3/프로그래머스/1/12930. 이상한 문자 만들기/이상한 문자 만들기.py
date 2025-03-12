def solution(s):
    answer, i = '', 0
    for c in s:
        i = -1 if c == ' ' else i
        answer += c.lower() if i % 2 == 1 else c.upper()
        i += 1
            
    return answer