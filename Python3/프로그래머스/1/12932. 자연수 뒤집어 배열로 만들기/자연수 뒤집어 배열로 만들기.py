def solution(n):
    rev = reversed(str(n))
    return list(map(int, list(rev)))