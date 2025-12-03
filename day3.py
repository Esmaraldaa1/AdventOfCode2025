def getMaxJoltageForBank(batteryLine):
    # batteryLine is a string of digits, for example "987654321111111"
    
    maxPairValue = 0      # largest two-digit value we can make in this bank
    lineLength = len(batteryLine)
    
    # Pick the first battery (left position)
    firstBattery = 0
    while firstBattery < lineLength:
        firstDigit = int(batteryLine[firstBattery])
        
        # Pick the second battery (right position)
        secondBattery = firstBattery + 1
        while secondBattery < lineLength:
            secondDigit = int(batteryLine[secondBattery])
            
            # Build the two-digit number: firstDigit is tens, secondDigit is ones
            pairValue = firstDigit * 10 + secondDigit
            
            # Update max if this pair is better
            if pairValue > maxPairValue:
                maxPairValue = pairValue
            
            secondBattery = secondBattery + 1
        
        firstBattery = firstBattery + 1
    
    return maxPairValue

def getMaxJoltageForBank12(batteryLine):
    # batteryLine is a string of digits, for example "987654321111111"
    totalDigitCount = len(batteryLine)
    targetDigitCount = 12

    # If the line is already 12 or shorter, just use all digits
    if totalDigitCount <= targetDigitCount:
        return int(batteryLine)

    # How many digits we are allowed to remove
    removeAllowed = totalDigitCount - targetDigitCount

    # List of chosen digits (characters)
    chosenDigits = []

    position = 0
    while position < totalDigitCount:
        currentDigit = batteryLine[position]

        # Try to remove smaller digits before this one
        # while:
        # - we can still remove digits
        # - we already have some chosen digits
        # - the last chosen digit is smaller than the current digit
        # - and we still can reach targetDigitCount after removing
        while (
            removeAllowed > 0 and
            len(chosenDigits) > 0 and
            chosenDigits[-1] < currentDigit and
            (len(chosenDigits) - 1) + (totalDigitCount - position) >= targetDigitCount
        ):
            # Remove the last digit
            chosenDigits.pop()
            removeAllowed = removeAllowed - 1

        # Keep the current digit
        chosenDigits.append(currentDigit)
        position = position + 1

    # If we still have too many digits, cut from the end
    while len(chosenDigits) > targetDigitCount:
        chosenDigits.pop()

    # Turn the chosen digits into a number
    joltageText = "".join(chosenDigits)
    return int(joltageText)


def solve():
    totalJoltage = 0
    
    # Read each bank (each line)
    with open("day3.txt") as file:
        for lineText in file:
            lineText = lineText.strip()
            
            # Skip empty lines, just in case
            if not lineText:
                continue
            
            # Get the best possible joltage for this bank
            bestForBank = getMaxJoltageForBank(lineText)
            totalJoltage = totalJoltage + bestForBank
    
    print(totalJoltage)




def solvePart2():
    totalJoltage = 0

    # Read each bank (each line)
    with open("day3.txt") as file:
        for lineText in file:
            lineText = lineText.strip()

            # Skip empty lines
            if not lineText:
                continue

            # Get the best possible 12-digit joltage for this bank
            bestForBank = getMaxJoltageForBank12(lineText)
            totalJoltage = totalJoltage + bestForBank

    print(totalJoltage)

if __name__ == "__main__":
    solve()
    solvePart2()
