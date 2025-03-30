def solution(s):
    dct = {
        "zero":"0",
        "one":"1",
        "two":"2",
        "three":"3",
        "four":"4",
        "five":"5",
        "six":"6",
        "seven":"7",
        "eight":"8",
        "nine":"9"
    }
    
    for d in dct:
        s = s.replace(d, dct[d])
    
    return int(s)