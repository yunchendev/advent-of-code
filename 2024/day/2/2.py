# part 1

with open("2024/day/2/input.txt", "r") as file: 
    lines = file.readlines()
    
reports = []

for line in lines:
    levels = []
    if line.strip(): 
        values = line.split()

        for val in values:
            levels.append(int(val))
        reports.append(levels)
            
# at this point the report array contains arrays of level

# check if level is strictly decreasing or increasing, if it is 'safe' 

def is_strictly_increasing(arr):
    if len(arr) < 2:
        return True
    
    prev = arr[0]
    
    for val in arr[1:]: 
        if val <= prev or val - prev > 3:
            return False
        prev = val
    return True


def is_strictly_decreasing(arr):
    if len(arr) < 2:
        return True
    
    prev = arr[0]
    
    for val in arr[1:]: 
        if val >= prev or prev - val > 3:
            return False
        
        prev = val
    return True

def asc_or_desc(levels):
    return is_strictly_decreasing(levels) or is_strictly_increasing(levels)

def is_safe(reports):
    safe_count = 0
    for levels in reports:
        if(asc_or_desc(levels)):
            safe_count += 1
        
    return safe_count

def is_safe_with_dampener(reports):
    safe_count = 0
    
    for levels in reports:
        if(asc_or_desc(levels)):
            safe_count += 1
        else:
            for i in range(len(levels)):
                modified_level = levels[:i] + levels[i+1:]
                if(asc_or_desc(modified_level)):
                    safe_count += 1
                    break
            
    return safe_count

print(f"Safe count: {is_safe(reports)}")

print(f"Safe count with dampender: {is_safe_with_dampener(reports)}")
    





            
            
            
            
            
            