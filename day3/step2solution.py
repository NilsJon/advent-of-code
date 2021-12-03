reader = open("input.txt", "r")
lines = reader.readlines()
currentLinesOxygen, currentLinesCO2 = lines, lines
scrubber_rating,oxygen_rating = 0, 0

for i in range(len(lines[0].strip())):
    lines_with_one_co,lines_with_one_ox = [],[]
    for line in currentLinesOxygen:
        if line[i] == '1':
            lines_with_one_ox.append(line)
    for line in currentLinesCO2:
        if line[i] == '1':
            lines_with_one_co.append(line)

    if len(lines_with_one_ox) >= len(currentLinesOxygen)/2:
        currentLinesOxygen = lines_with_one_ox
    else:
        currentLinesOxygen = [entry for entry in currentLinesOxygen if entry not in lines_with_one_ox]

    if len(lines_with_one_co) < len(currentLinesCO2)/2:
        currentLinesCO2 = lines_with_one_co
    else: currentLinesCO2 = \
        [entry for entry in currentLinesCO2 if entry not in lines_with_one_co]

    if len(currentLinesCO2) == 1: scrubber_rating = int(currentLinesCO2[0].strip(),2)
    if len(currentLinesOxygen) == 1: oxygen_rating = int(currentLinesOxygen[0].strip(),2)

print("Solution part 2: %d" %(oxygen_rating * scrubber_rating))


    