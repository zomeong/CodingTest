def solution(n, m):

    if n > m:
        n, m = m, n
        
    for i in range(1, n + 1):
        if n % i == 0 and m % i == 0:
            gcd = i
            
    lcd = n * m // gcd
    
    return [gcd, lcd]