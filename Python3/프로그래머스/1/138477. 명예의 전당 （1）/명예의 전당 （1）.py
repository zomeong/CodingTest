def solution(k, score):
    answer = [score[0]]
    honer = score[:2]
    
    if (honer[0] > honer[1]):
        answer.append(honer[1])
    else:
        answer.append(honer[0])
        
    for i in range(2, len(score)):
        honer.append(score[i])
        honer.sort(reverse=True)
        
        if len(honer) < k:
            answer.append(honer[len(honer) - 1])
        else:
            answer.append(honer[k - 1])
    
    return answer