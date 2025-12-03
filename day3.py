with open('day3input.txt', 'r') as file:
    input = file.readlines()

def calc(inputArray, digitcount):
    count = 0

    for bank in inputArray:
        
        bank = bank.strip()
        digits = []
        currentindex = -1
        remaining = digitcount
        
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
            
        count += int(result)

    return count

print('Part 1: ' + str(calc(input,2)))
print('Part 2: ' + str(calc(input,12)))