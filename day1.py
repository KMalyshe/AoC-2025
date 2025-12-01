with open('day1input.txt', 'r') as file:
    input = file.readlines()

safe = 50
p1count = 0
p2count = 0

for line in input:
    direction = line[0]
    turns = int(line[1:])
    
    if direction == 'L':
        for i in range(1, turns + 1):
            next = (safe - i) % 100
            if next == 0:
                p2count += 1
        safe = (safe - turns) % 100
    else:
        for i in range(1, turns + 1):
            next = (safe + i) % 100
            if next == 0:
                p2count += 1
        safe = (safe + turns) % 100
    
    if safe == 0:
        p1count += 1

print('Part 1: ' + str(p1count))
print('Part 2: ' + str(p2count))