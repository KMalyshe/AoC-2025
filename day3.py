with open('day3input.txt', 'r') as file:
    input = file.readlines()

count = 0

# Part 1
for bank in input:
    
    bank = bank.strip()
    firstdigit = 0
    index = 0
    
    for i in reversed(range(10)):
        index = bank.find(str(i))
        if index != len(bank)-1 and index != -1:
            firstdigit = i
            break

    for i in reversed(range(10)):
        if bank.find(str(i), index+1) != -1:
            count += int(str(firstdigit) + str(i))
            break

print(count)

# Part 2 (I'm too lazy to figure out how to combine them into one :3)
count = 0

for bank in input:
    
    bank = bank.strip()
    digits = []
    currentindex = -1
    remaining = 12
    
    running = True
    while(running):
        for i in reversed(range(10)):
            index = bank.find(str(i), currentindex+1)
            if index != -1 and len(bank)-index-1 >= remaining-1:
                digits.append(i)
                remaining -= 1
                currentindex = index
                break
        if remaining == 0:
            running = False
    
    result = ''
    for digit in digits:
        result += str(digit)
    
    print('Added ' + result)
    count += int(result)

print(count)