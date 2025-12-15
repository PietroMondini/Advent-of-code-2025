def main():
    with open("day01 - Secret entrance/input.txt") as f:
        rotations = [line.strip() for line in f.readlines()]

    part1(rotations)
    part2(rotations)

def part1(rotations):
    DIAL = 50
    zeros = 0

    for rotation in rotations:
        DIAL = rotate(DIAL, rotation[0], int(rotation[1:]))
        zeros += 1 if DIAL == 0 else 0
    
    print("Part 1:", zeros)

def part2(rotations):
    DIAL = 50
    zeros = 0

    for rotation in rotations:
        DIAL, x = rotateAndCount(DIAL, rotation[0], int(rotation[1:]))
        zeros += x

    print("Part 2:", zeros)

def rotate(dial, direction, steps):
    if direction == "L":
        dial = (dial - steps) % 100
    else:
        dial = (dial + steps) % 100
    return dial

def rotateAndCount(dial, direction, steps):
    x = 0

    if direction == "L":
        if dial - steps <= 0:
            x = (steps - dial) // 100
            if dial != 0:
                x += 1
        dial = (dial - steps) % 100
    else:
        if dial + steps >= 100:
            x = 1 + (steps - (100 - dial)) // 100
        dial = (dial + steps) % 100

    return dial, x

if __name__ == "__main__":
    main()