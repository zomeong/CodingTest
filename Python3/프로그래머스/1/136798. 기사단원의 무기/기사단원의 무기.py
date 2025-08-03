def solution(number, limit, power):
    mea = []
    
    for i in range(1, number + 1):
        cnt = 0
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                cnt += 2
            if j * j == i:
                cnt -= 1
        mea.append(cnt)
                
    for i in range(len(mea)):
        if mea[i] > limit:
            mea[i] = power
    
    return sum(mea)