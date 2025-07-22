def solution(cards1, cards2, goal):
    i, j = 0, 0
    
    for g in goal:
        if(len(cards1) > i and g == cards1[i]):
            i+=1
        elif(len(cards2) > j and g == cards2[j]):
            j+=1
        else:
            return "No"
        
    return "Yes"