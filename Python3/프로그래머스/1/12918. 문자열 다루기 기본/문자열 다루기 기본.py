def solution(s):
    return True if (len(s) == 4 or len(s) == 6) and str.isdigit(s) else False