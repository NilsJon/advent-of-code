horizontal = 0
depth = 0
reader = open("input.txt", "r")
for line in reader:
    words = line.split(" ")
    direction = words[0]
    if direction == "down":
        depth += int(words[1])
     
    if direction == "up":
        depth -= int(words[1])

    if direction == "forward":
        horizontal += int(words[1])

print(depth*horizontal)
     