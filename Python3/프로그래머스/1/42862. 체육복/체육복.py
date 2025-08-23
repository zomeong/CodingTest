def solution(n, lost, reserve):
    answer = n - len(lost)
    lost.sort()
    reserve.sort()
    
    for l in lost:
        if l in reserve:
            answer += 1
            reserve.remove(l)
            lost[lost.index(l)] = -1
    
    for l in lost:
        if l == -1:
            continue
        elif l - 1 in reserve:
            answer += 1
            reserve.remove(l-1)
            
        elif l + 1 in reserve:
            answer += 1
            reserve.remove(l+1)
    
    return answer