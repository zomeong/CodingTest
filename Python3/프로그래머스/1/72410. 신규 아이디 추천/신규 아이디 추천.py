import re

def solution(new_id):
    
    new_id = new_id.lower()
    new_id = re.sub(r'[^a-z0-9\-_.]', '', new_id)
    new_id = re.sub(r'\.+', '.', new_id)
    
    if new_id[0] == ".":
        new_id = new_id[1:]
    if len(new_id) > 0 and new_id[-1] == ".":
        new_id = new_id[:-1]
        
    if len(new_id) == 0:
        new_id = "a"
        
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:-1]
            
    if len(new_id) < 3:
        char = new_id[-1]
        for i in range(3 - len(new_id)):
            new_id += char
    
    return new_id