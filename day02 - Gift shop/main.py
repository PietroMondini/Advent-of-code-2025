import re

def main():
    with open("day02 - Gift shop/input.txt") as f:
        line = f.readline()
        idRanges = line.strip().split(",")
        p1(idRanges)
        p2(idRanges)

# Part 1

def p1(idRanges):
    invalidCount = 0
    for fstID, lstID in (r.split("-") for r in idRanges):
        invalidCount += checkRange(int(fstID), int(lstID))
    print("Part 1:", invalidCount)

def checkRange(fstID, lstID):
    invalidCount = 0
    for id in range(fstID, lstID + 1):
        invalidCount += id if isInvalid(id) else 0
    return invalidCount

def isInvalid(id):
    return bool(re.fullmatch(r'(.+)\1', str(id)))

# Part 2

def p2(idRanges):
    invalidCount = 0
    for fstID, lstID in (r.split("-") for r in idRanges):
        invalidCount += checkRange_v2(int(fstID), int(lstID))
    print("Part 2:", invalidCount)

def checkRange_v2(fstID, lstID):
    invalidCount = 0
    for id in range(fstID, lstID + 1):
        invalidCount += id if isInvalid_v2(id) else 0
    return invalidCount

def isInvalid_v2(id):
    return bool(re.fullmatch(r'(.+)\1+', str(id)))

if __name__ == "__main__":
    main()