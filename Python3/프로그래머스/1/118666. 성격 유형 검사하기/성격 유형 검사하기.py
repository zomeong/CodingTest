def solution(survey, choices):
    answer = ''
    MBTI = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    
    for s, c in zip(survey, choices):
        if c < 4:
            MBTI[s[0]] += 4 - c
        else:
            MBTI[s[1]] += c - 4
            
    answer += "T" if MBTI["R"] < MBTI["T"] else "R"
    answer += "F" if MBTI["C"] < MBTI["F"] else "C"
    answer += "M" if MBTI["J"] < MBTI["M"] else "J"
    answer += "N" if MBTI["A"] < MBTI["N"] else "A"
    
    return answer