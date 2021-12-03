reader = open("input.txt", "r")
firstLine = reader.readline()
sumBits = []

for c in firstLine:
    if c != '\n':
        sumBits.append(0)
j = 1
for line in reader:
    j += 1
    for i in range(0, len(line)):
        if line[i] != '\n':
            sumBits[i] += int(line[i])
            

print(sumBits)
result = [1 if x > (j/2) else 0 for x in sumBits]
print(result)

print(2663 * 1432)

