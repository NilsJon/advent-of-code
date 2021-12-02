reader = open("input.txt", "r")
counter = 0
nums = []
for line in reader:
    nums.append(int(line))
    
for x, y in zip(nums, nums[3:]):
    if x < y:
        counter += 1

print(counter)