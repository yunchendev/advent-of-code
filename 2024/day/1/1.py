# part 1
with open("2024/day/1/input.txt", "r") as file: 
    lines = file.readlines()

column1 = []
column2 = []

for line in lines:
    if line.strip(): 
        values = line.split()
        column1.append(int(values[0]))
        column2.append(int(values[1]))

column1.sort()
column2.sort()

total_difference = 0
for i in range(len(column1)):
    total_difference += abs(column1[i] - column2[i])

print("Total Difference:", total_difference)


# part 2

similarity_sum = 0
for val1 in column1:
    duplicate_count = 0
    for val2 in column2:
        if val1 == val2:
            duplicate_count += 1
            
    similarity_sum += val1 * duplicate_count

print(similarity_sum)
            

