import math
from collections import defaultdict

def solution(fees, records):
    
    answer = []
    cars = defaultdict(lambda: {"IN": None, "TIME": 0})
    defalut_time, defalut_fee, per_time, per_fee = fees
    
    for r in records:
        time, number, type_ = r.split()
        minutes = int(time[:2]) * 60 + int(time[3:])    # 분으로 환산
        
        if type_ == "IN":
            # 입차시 시간 기록
            cars[number]["IN"] = minutes    
        else:
            # 출차시 주차 시간 누적 후 입사 기록 초기화 
            out_time = minutes
            parking_time = out_time - cars[number]["IN"]
            cars[number]["TIME"] += parking_time
            cars[number]["IN"] = None
                 
    for number in sorted(cars.keys()):
        # 출차 기록 없는 차량 기본값으로 주차 기록 누적
        end_time = 23 * 60 + 59
        if cars[number]["IN"] is not None:
            cars[number]["TIME"] += end_time - cars[number]["IN"]
            
        # 주차비 계산
        parking_time = cars[number]["TIME"]
        fee = defalut_fee

        if parking_time > defalut_time:
            fee += math.ceil((parking_time - defalut_time) / per_time) * per_fee
            
        answer.append(fee)
    
    return answer