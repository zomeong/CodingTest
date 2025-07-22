def solution(cards1, cards2, goal):
    i, j, result = 0, 0, []
    c1, c2 = True, True
    
    for g in goal:
        if(c1 and g == cards1[i]):
            i+=1
            result.append(g)
            if(i >= len(cards1)):
                c1 = False
        elif(c2 and g == cards2[j]):
            j+=1
            result.append(g)
            if(j >= len(cards2)):
                c2 = False
    
    if result == goal:
        return "Yes"
    else:
        return "No"