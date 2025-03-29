# A = 65, Z = 90, a = 97, z = 122

def solution(s, n):
    answer = ''
    
    for c in s:
        o = ord(c)
        on = o + n
        
        if o == 32:
            on = o
        elif (o < 91 and on > 90) or on > 122:
            on -= 26
            
        answer += chr(on)
    
    return answer