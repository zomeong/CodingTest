def solution(absolutes, signs):
    for i in range(0, len(signs)):
        if(signs[i] == False):
            absolutes[i] = -absolutes[i]
        
    return sum(absolutes)