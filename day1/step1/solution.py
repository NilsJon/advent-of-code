reader = open("input.txt", "r")
counter = 0
lastNumber = None;
for line in reader:
    nr = int(line)
    if lastNumber is None:
        lastNumber = nr
    elif lastNumber < nr:
        counter += 1
    lastNumber = nr
        
print(counter)