def isInvalidID(number):
    # Turn number into string
    textNumber = str(number)

    # Count how many characters are in the number
    characterCount = len(textNumber)

    # Check if characterCount is even
    temp = characterCount
    while temp > 1:
        temp -= 2

    # If we end at 1, it means the number is odd and we cannot split into equal halves
    if temp == 1:
        return False

    # Find half-size
    halfSize = 0
    current = 0
    while current < characterCount:
        current += 2
        halfSize += 1
    # Now halfSize is the length of each half

    # Split the number into two halves
    firstHalf = textNumber[:halfSize] 
    secondHalf = textNumber[halfSize:]

    # The ID is invalid if the halves are identical
    return firstHalf == secondHalf


# PART 2
def isInvalidIDPart2(number):
    # Turn the number into a string
    textNumber = str(number)

    # Count how many characters the number has
    characterCount = len(textNumber)

    # If it has only 1 character, it cannot be made from a repeating pattern
    if characterCount == 1:
        return False

    # Try every possible block size (length of the repeated pattern)
    blockSize = 1
    while blockSize < characterCount:
        
        # Check if total length can be split into full blocks
        tempLength = characterCount
        blockCount = 0

        while tempLength > 0:
            tempLength = tempLength - blockSize
            blockCount = blockCount + 1

        # If tempLength is 0, it splits evenly AND at least 2 blocks are needed
        if tempLength == 0 and blockCount >= 2:

            # Compare all blocks with the first block
            pattern = textNumber[0:blockSize]
            startPosition = blockSize
            allSame = True

            while startPosition < characterCount:
                currentBlock = textNumber[startPosition:startPosition + blockSize]
                if currentBlock != pattern:
                    allSame = False
                    break
                startPosition = startPosition + blockSize

            if allSame:
                return True

        # Try next block size
        blockSize = blockSize + 1

    # No valid repeating pattern found
    return False



def solve():
    total = 0

    # Read the single line of ranges
    with open("input2.txt") as file:
        line = file.read().strip()

    # Split into separate ranges
    ranges = line.split(",")

    for rangeItem in ranges:
        # Example: "11-22"
        parts = rangeItem.split("-")
        startID = int(parts[0])
        endID = int(parts[1])

        # Check each ID in the range
        for number in range(startID, endID + 1):
            if isInvalidID(number):
                total += number

    print(total)


def solvePart2():
    total = 0

    # Read the single line of ranges
    with open("day2.txt") as file:
        line = file.read().strip()

    # Split into separate ranges
    ranges = line.split(",")

    for rangeText in ranges:
        # Example: "11-22"
        parts = rangeText.split("-")
        startID = int(parts[0])
        endID = int(parts[1])

        # Check each ID in the range
        for number in range(startID, endID + 1):
            if isInvalidIDPart2(number):
                total = total + number

    print(total)


if __name__ == "__main__":
    solve()
    solvePart2()