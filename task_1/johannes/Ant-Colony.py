import numpy as np

# Params
height = 10
width = 10
grid = np.random.randint(0, 10, size=(height, width))  # create grid
pheromoneDeposits = 0.1 * np.ones(shape=(height, width))  # create pheromone deposit grid filled with one
start = [0, 0]
end = [height - 1, width - 1]
current = start
iterations = 1000

# results Store the results of the ants into here
results = []

print(grid)


def isValidPosition(position, visitedLocations):
    if (height > position[0] >= 0 and width > position[1] >= 0) and not ([position[0], position[1]] in visitedLocations):
        return True
    else:
        return False


def availablePositions(current, visitedLocations):
    global height, width
    positions = []

    p = [current[0] + 1, current[1]]
    if isValidPosition(p, visitedLocations):
        positions.append(p)

    p = [current[0] - 1, current[1]]
    if isValidPosition(p, visitedLocations):
        positions.append(p)

    p = [current[0], current[1] + 1]
    if isValidPosition(p, visitedLocations):
        positions.append(p)

    p = [current[0], current[1] - 1]
    if isValidPosition(p, visitedLocations):
        positions.append(p)

    return positions


def calculateScore(positions):
    global pheromoneDeposits, grid
    gridScores = []
    for pos in positions:
        if grid[pos[0], pos[1]] == 0:
            score = 0
        else:
            score = pheromoneDeposits[pos[0], pos[1]] * (1 / grid[pos[0], pos[1]])
        gridScores.append(score)
    return gridScores


# iterations
for i in range(iterations):
    print("Generation ", i + 1)
    # reset
    visitedLocations = []
    isAntAlive = True
    finished = False
    current = start
    while isAntAlive:

        # check available positions
        positions = availablePositions(current, visitedLocations)
        # If there are no positions available
        if len(positions) == 0:
            isAntAlive = False
            finished = False

            # time taken
            timeTaken = 0
            for square in visitedLocations:
                timeTaken += grid[square[0], square[1]]
            result = {"generation": i, "timeTaken": timeTaken, "pathTaken": visitedLocations, "finished": finished}
            results.append(result)
            continue  # return to the loop

        # check their score
        scores = calculateScore(positions)
        # calculate probability of going to that square by the score
        probabilities = []
        probabilityTotal = 0
        for score in scores:
            probabilities.append(score / len(scores))
            probabilityTotal += score / len(scores)

        for j in range(len(probabilities)):
            if np.isinf(probabilities[j]):
                probabilities[j] = 0
        # print(probabilities)

        # move to one based on chance
        randomNumber = np.random.uniform(0, probabilityTotal)
        indexOfChosen = 0
        tempTotals = probabilities[0]
        for p in probabilities:
            if randomNumber <= tempTotals:
                break
            if indexOfChosen == len(probabilities) - 1:
                break
            tempTotals += p
            indexOfChosen += 1

        # change current to that, add to visited squares
        visitedLocations.append(current)
        current = positions[indexOfChosen]

        if current[0] == end[0] and current[1] == end[1]:
            # ADD PHEROMONES TO DEPOSITED
            # shorter the path, the higher the deposit
            # 1 / average path length

            # calculate the time taken on this path
            timeTaken = 0
            for square in visitedLocations:
                timeTaken += grid[square[0], square[1]]

            # calculate the amount of pheromones to deposit
            amountOfPheromone = 10 / timeTaken

            # deposit the pheromones
            for square in visitedLocations:
                pheromoneDeposits[square[0], square[1]] += amountOfPheromone

            isAntAlive = False
            finished = True

            result = {"generation": i, "timeTaken": timeTaken, "pathTaken": visitedLocations, "finished": finished}
            results.append(result)
            continue

        # if it reaches the end break the loop

# find the shortest out off the generations
if len(results) > 0:
    shortestResult = results[0]
    for result in results:
        if result["finished"]:
            if result["timeTaken"] < shortestResult["timeTaken"]:
                shortestResult = result

    if shortestResult["finished"]:
        print("Shortest path found was:\n    Generation:", shortestResult["generation"], "\n    Time Taken (grid time): ", shortestResult["timeTaken"], "\n    Path: ", shortestResult["pathTaken"])
    else:
        print("Shortest path not found")
