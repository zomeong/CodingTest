from collections import defaultdict

def solution(friends, gifts):
    answer = 0
    gift_dict = defaultdict(lambda: defaultdict(int))
    gift_count, result = {}, []
    
    # 주고받은 선물 딕셔너리
    for g in gifts:
        a, b = g.split()
        
        gift_dict[a][b] += 1
        gift_dict[a]['total'] += 1
        
    # 선물 지수 딕셔너리
    for f in friends:
        give = gift_dict.get(f,{}).get('total', 0)
        take = sum(gift.get(f, 0) for gift in gift_dict.values())
        gift_count[f] = give-take
        
    # 받을 선물 계산
    for f1 in friends:
        cnt = 0
        for f2 in friends:
            if f1 == f2:
                continue
                
            give = gift_dict.get(f1, {}).get(f2, 0)
            take = gift_dict.get(f2, {}).get(f1, 0)
            
            if give > take or (give == take and gift_count[f1] > gift_count[f2]):
                cnt += 1
                
        answer = max(cnt, answer)
    
    return answer