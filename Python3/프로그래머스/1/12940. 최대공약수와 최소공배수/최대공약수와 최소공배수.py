def solution(n, m):

    gcd = 1
    if n > m:
        n, m = m, n
        
    for i in range(n, 0, -1):
        if n % i == 0 and m % i == 0:
            gcd = i
            break
            
    lcd = n * m / gcd
    
    return [gcd, lcd]