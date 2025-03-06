def solution(arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):
        a = []
        for i, j in zip(a1, a2):
            a.append(i + j)
        answer.append(a)
        
    return answer