from datetime import datetime
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    answer = []
    term_map = {}
    today = datetime.strptime(today, "%Y.%m.%d")
    
    for t in terms:
        char, month = t.split()
        term_map[char] = month
        
    for i, p in enumerate(privacies, start=1):
        date, t = p.split()
        date = datetime.strptime(date, "%Y.%m.%d")
        month = int(term_map[t])
        deadline = date + relativedelta(months=month)
        
        if deadline <= today:
            answer.append(i)
    
    return answer