def solution(s):
    dct = {
        "zero":"0",
        "one":"1",
        "two":"2",
        "three":"3",
        "four":"4",
        "five":"5",
        "six":"6",
        "seven":"7",
        "eight":"8",
        "nine":"9"
    }
    pos = []
    answer = ""
    
    for d in dct:
        idx = s.find(d)
        while idx != -1:
            pos.append([idx, dct[d]])
            idx = s.find(d, idx + 1)
            
        idx = s.find(dct[d])
        while idx != -1:
            pos.append([idx, dct[d]])
            idx = s.find(dct[d], idx + 1)
            
    pos.sort()
    
    for p in pos:
        answer += p[1]
    
    return int(answer)