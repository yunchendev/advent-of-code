import re

with open("2024/day/3/input.txt", "r") as file: 
    lines = file.readlines()

def calculate_mul_sum(memory):
  # regex pattern for finding string mul(x,y) and a list of tuple (x, y)
  pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

  matches = re.findall(pattern, memory)
   
  total_sum = 0
  for x, y in matches:
    sum = int(x) * int(y)
    total_sum += sum

  return total_sum

sum = 0
for line in lines:
   sum += calculate_mul_sum(line)

print(sum)
