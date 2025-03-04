def solution(s):
    i = len(s) // 2
    return s[i-1:i+1] if len(s) % 2 == 0 else s[i]