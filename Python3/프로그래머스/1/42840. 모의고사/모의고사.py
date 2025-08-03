def solution(answers):
    
    cnt1, cnt2, cnt3 = 0, 0, 0
    one = [1, 2, 3, 4, 5] * 2000
    two = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    
    for i in range(0, len(answers)):
        if answers[i] == one[i]:
            cnt1+=1
        if answers[i] == two[i]:
            cnt2+=1
        if answers[i] == three[i]:
            cnt3+=1
        
    values = [-1, cnt1, cnt2, cnt3]
    max_val = max(values)
    
    return [i for i, v in enumerate(values) if v == max_val]