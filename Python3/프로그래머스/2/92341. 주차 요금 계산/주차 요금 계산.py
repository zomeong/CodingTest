import math
from collections import defaultdict

def solution(fees, records):
    
    answer = []
    cars = defaultdict(lambda: {"IN": None, "TIME": 0})
    defalut_time, defalut_fee, per_time, per_fee = fees
    
    for r in records:
        time, number, type_ = r.split()
        minutes = int(time[:2]) * 60 + int(time[3:])
        
        if type_ == "IN":
            cars[number]["IN"] = minutes
        else:
            out_time = minutes
            parking_time = out_time - cars[number]["IN"]
            cars[number]["TIME"] += parking_time
            cars[number]["IN"] = None
                 
    for number in sorted(cars.keys()):
        end_time = 23 * 60 + 59
        if cars[number]["IN"] is not None:
            cars[number]["TIME"] += end_time - cars[number]["IN"]
            
        parking_time = cars[number]["TIME"]
        fee = defalut_fee

        if parking_time > defalut_time:
            fee += math.ceil((parking_time - defalut_time) / per_time) * per_fee
            
        answer.append(fee)
    
    return answer