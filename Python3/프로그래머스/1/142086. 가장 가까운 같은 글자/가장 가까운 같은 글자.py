def solution(s):
    answer, dct = [], {}
    
    for i in range(len(s)):
        c = s[i]
        if dct.get(c) is None:
            answer.append(-1)
        else:
            answer.append(i - dct[c])
        dct[c] = i
    
    return answer