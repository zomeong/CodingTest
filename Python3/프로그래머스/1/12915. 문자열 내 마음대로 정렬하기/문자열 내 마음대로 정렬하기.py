def solution(strings, n):
    strings.sort(key=lambda x: (x[n], x[0:]))
    return strings