def solution(sizes):
    r, c = 0, 0
    
    for x, y in sizes:
        if x < y:
            x, y = y, x
            
        r = max(r, x)
        c = max(c, y)
    
    return r * c