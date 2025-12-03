with open('day2input.txt', 'r') as file:
    input = file.readlines()
    
ranges = input[0].split(',')
p1count = 0
p2count = 0

for bracket in ranges:
    l = int(bracket.split('-')[0])
    r = int(bracket.split('-')[1])
    
    for i in range(l, r+1):
        lefthalf = str(i)[:len(str(i))//2]
        righthalf = str(i)[len(str(i))//2:]
        if lefthalf == righthalf:
            p1count += i
        
        pattern = ''
        for digit in str(i):
            pattern += digit
            patternAmount = str(i).count(pattern)
            if patternAmount*len(pattern) == len(str(i)) and patternAmount > 1:
                p2count += i
                print('Added ' + str(i))
                break
            

print('Part 1:' + str(p1count))
print('Part 2:' + str(p2count))
        
