def solution(n, k):
    answer = 0
    digits = ""
    
    # 진수 변환
    while n > 0:
        digits += str(n % k)
        n //= k
    dig = ''.join(reversed(digits))
    
    # 구분점 0
    parts = dig.split('0')
    prims = [int(p) for p in parts if p]
    
    # 소수 판별
    for p in prims:
        if is_prime(p):
            answer += 1
    
    return answer

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True