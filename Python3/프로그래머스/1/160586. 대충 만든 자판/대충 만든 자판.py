def solution(keymap, targets):
    answer = []
    dic = {}
    
    for key in keymap:
        for k in key:
            idx = key.index(k) + 1
            dic[k] = min(idx, dic.get(k, 101))
            
    cnt = 0
    for tar in targets:
        
        for t in tar:
            val = dic.get(t, -1)
            if val == -1:
                cnt = -1
                break
            cnt += val
                
        answer.append(cnt)
        cnt = 0
    
    return answer