import math

# Helperfunction: count how many times we hit 0 during the rotation
def countHits(position: int, direction: str, distance: int) -> int:
    # Right rotation
    if direction == "R":
        # If already at 0, hit every 100 steps
        if position == 0:
            return distance // 100
        
        # Steps needed to reach 0 the first time
        first = 100 - position

        # If we cannot reach 0 in this rotation
        if first > distance:
            return 0
        
        # 1 for the first hit, plus hits every 100 steps after
        return 1 + (distance - first) // 100
    
    # Left rotation
    elif direction == "L":
        # If already at 0, hit every 100 steps
        if position == 0:
            return distance // 100
        
        # Steps needed to reach 0 the first time 
        first = position

        # If we cannot reach 0 in this rotation  
        if first > distance:
            return 0
        
        # 1 for the first hit, plus hits every 100 steps after
        return 1 + (distance - first) // 100
    
    # Invalid direction
    else:
        raise ValueError(f"Unknown direction: {direction}")

# PART 1
def solvePart1():
    position = 50      # starting position
    countZero = 0      # how much yimes we end at 0

    with open("input.txt") as file:
        for line in file:
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            direction = line[0]       # First char: 'L' or 'R'
            distance = int(line[1:])  # Remaining characters: number (everything after the first character)

            # Update position based on direction
            if direction == "R":
                position = (position + distance) % 100
            elif direction == "L":
                position = (position - distance) % 100
            else:
                raise ValueError(f"Unknown direction: {direction}")
            
            # Count if final position is 0
            if position == 0:
                countZero += 1

    print(countZero)


# PART 2
def solvePart2():
    position = 50   # starting position
    totalHits = 0   # total hits at 0 (during AND after rotation)

    with open("input.txt") as file:
        for line in file:
            line = line.strip()

            # Skip empty lines
            if not line:
                continue
            
            direction = line[0]         # 'L' or 'R'
            distance = int(line[1:])    # number of steps

            # Count all 0 hits during the rotation
            hits = countHits(position, direction, distance)
            totalHits += hits

            # Update position after the rotation (like part 1)
            if direction == "R":
                position = (position + distance) % 100
            elif direction == "L":
                position = (position - distance) % 100
            else:
                raise ValueError(f"Unknown direction: {direction}")

    print(totalHits)

# Run both parts
if __name__ == "__main__":
    solvePart1()
    solvePart2()

