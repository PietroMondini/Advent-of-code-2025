def main():
    with open("day03 - Lobby/input.txt") as f:
        banks = f.read().splitlines()
    
    p1(banks)
    p2(banks)

def p1(banks):
    joltage = 0

    for bank in range(0,len(banks)):
        max, maxDx = 0, 0
        for battery in range(0,len(banks[bank])):
            if max == 9 and maxDx == 9:
                break
            elif max != 9 and int(banks[bank][battery]) > max and battery != len(banks[bank])-1:
                max = int(banks[bank][battery])
                maxDx = 0
            elif maxDx != 9 and int(banks[bank][battery]) > maxDx:
                maxDx = int(banks[bank][battery])       
        joltage += int(str(max) + str(maxDx))      
    print("Part 1 joltage:", joltage)

def p2(banks):
    joltage = 0
    n = 12

    for bank in range(0, len(banks)):
        j = bankJoltage(banks[bank], n)
        joltage += bankJoltage(banks[bank], n)
    
    print("Part 2 joltage:", joltage)

def bankJoltage(bank, n):
    return chooseBattery(bank, n, "")

def chooseBattery(bank, n, joltage):
    if n == 0:
        return int(joltage)
    
    max = 0
    for batt in range(0,len(bank)-n+1):
        
        battery = int(bank[batt])
        if battery == 9:
            return chooseBattery(bank[batt+1:], n-1, joltage + "9")
        elif battery > int(bank[max]):
            max = batt
    return chooseBattery(bank[max+1:], n-1, joltage + str(bank[max]))

if __name__ == "__main__":
    main()