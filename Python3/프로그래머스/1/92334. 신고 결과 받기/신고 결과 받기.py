from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    count = defaultdict(int)
    users = defaultdict(set)
    mail = defaultdict(int)
    
    for r in report:
        a, b = r.split()
        
        if a not in users[b]:
            count[b] += 1
            users[b].add(a)
    
    for id_ in id_list:
        if count[id_] >= k:
            for u in users[id_]:
                mail[u] += 1
    
    for id_ in id_list:
        answer.append(mail[id_])
    
    return answer