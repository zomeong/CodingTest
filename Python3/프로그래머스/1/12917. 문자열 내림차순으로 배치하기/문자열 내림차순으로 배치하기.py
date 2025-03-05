def solution(s):
    l, u =  [], []
    
    for i in s:
        l.append(i) if i.islower() else u.append(i)
            
    l = sorted(l, reverse=True)
    u = sorted(u, reverse=True)
    return "".join(l) + "".join(u)
            