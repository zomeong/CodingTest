def solution(s):
    answer, dct = [], {}
    
    for i in range(len(s)):
        c = s[i]
        if dct.get(c) is None:
            dct[c] = i
            answer.append(-1)
        else:
            idx = dct[c]
            dct[c] = i
            answer.append(i - idx)
    
    return answer