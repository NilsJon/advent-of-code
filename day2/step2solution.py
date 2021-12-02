horizontal = 0
depth = 0
aim = 0
reader = open("input.txt", "r")
for line in reader:
    words = line.split(" ")
    direction = words[0]
    if direction == "down":
        aim += int(words[1])
        #depth += int(words[1])
     
    elif direction == "up":
        aim -= int(words[1])

    else:
        steps = int(words[1])
        horizontal += steps
        depth += aim*steps

print(depth*horizontal)
     