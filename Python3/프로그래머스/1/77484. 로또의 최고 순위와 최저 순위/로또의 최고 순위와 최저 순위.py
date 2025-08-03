from collections import Counter

def solution(lottos, win_nums):

    zero = sum(1 for l in lottos if l == 0)
    
    common = Counter(lottos) & Counter(win_nums)
    same = sum(common.values())

    return [add_rank(same + zero), add_rank(same)]

def add_rank(n):
    ranks = [-1, 6, 5, 4, 3, 2]
    if n in ranks:
        return ranks.index(n)
    else:
        return 6