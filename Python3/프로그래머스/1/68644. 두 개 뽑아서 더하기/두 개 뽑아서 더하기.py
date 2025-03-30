def solution(numbers):
    s, l = set(), len(numbers)
    
    for n in numbers:
        for m in range(numbers.index(n) + 1, l):
            s.add(n + numbers[m])
    
    return sorted(list(s))