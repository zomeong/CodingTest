def solution(a, b, n):
    result = 0
    
    while n >= a:
        give = n // a * a
        receive = n // a * b
        n -= give - receive
        result += receive
        
    return result

def bottle(a, b, n, result):
    if n < a:
        return result
    
    give = n // a * a
    receive = n // a * b
    return bottle(a, b, n - give + receive, result + receive)