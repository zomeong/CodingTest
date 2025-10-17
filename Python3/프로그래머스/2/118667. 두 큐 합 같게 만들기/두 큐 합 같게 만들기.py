from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1, q2 = deque(queue1), deque(queue2)
    sq1, sq2 = sum(q1), sum(q2)
    if (sq1 + sq2) % 2 != 0: return -1
    
    while answer < len(queue1) * 3:
        if len(q1) == 0 or len(q2) == 0:
            return -1
        
        if sq1 == sq2:
            break
        elif sq1 > sq2:
            p = q1.popleft()
            q2.append(p)
            sq1 -= p
            sq2 += p
        else:
            p = q2.popleft()
            q1.append(p)
            sq1 += p
            sq2 -= p
        
        answer += 1
        
    answer = -1 if answer == len(queue1) * 3 else answer
    
    return answer