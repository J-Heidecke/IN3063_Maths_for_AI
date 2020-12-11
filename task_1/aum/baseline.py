import numpy as np

# create a height/width grid
height = 4
width = 4
grid = np.random.randint(0, 10, size=(height, width))
visitedPositions = []  # Visited Positions
startPosition = [0, 0]
endPosition = [height-1, width-1]

currentPosition = startPosition


# get the available locations, as of now, only right and down
def getAvailablePositions():
    global currentPosition
    positions = []

    # Right
    x = currentPosition[0] + 1
    y = currentPosition[1]
    if (height > x >= 0 and width > y >= 0) and not ([x, y] in visitedPositions):
        positions.append([x, y])

    # # Left
    # x = currentPosition[0] - 1
    # y = currentPosition[1]
    # if (height > x >= 0 and width > y >= 0) and not ([x, y] in visitedPositions):
    #     positions.append([x, y])

    # Down
    x = currentPosition[0]
    y = currentPosition[1] + 1
    if (height > x >= 0 and width > y >= 0) and not ([x, y] in visitedPositions):
        positions.append([x, y])

    # # Up
    # x = currentPosition[0]
    # y = currentPosition[1] - 1
    # if (height > x >= 0 and width > y >= 0) and not ([x, y] in visitedPositions):
    #     positions.append([x, y])

    return positions


totalTime = 0
while currentPosition != endPosition:
    availablePositions = getAvailablePositions()

    # get the lowest time
    leastPossibleTimePosition = [-1, -1]
    for position in availablePositions:
        if leastPossibleTimePosition == [-1, -1]:
            leastPossibleTimePosition = position
            continue
        if grid[position[0], position[1]] < grid[leastPossibleTimePosition[0], leastPossibleTimePosition[1]]:
            leastPossibleTimePosition = position
    if len(availablePositions) == 0:
        leastPossibleTimePosition = currentPosition
    # Go to the lowest score
    visitedPositions.append(currentPosition)
    totalTime += grid[currentPosition[0], currentPosition[1]]
    currentPosition = leastPossibleTimePosition
    print(currentPosition)

visitedPositions.append(currentPosition)

print()
print("Grid:")
print(grid)
print("Result:")
print("Total Time Spent on Squares: ", totalTime)
print("Path", visitedPositions)