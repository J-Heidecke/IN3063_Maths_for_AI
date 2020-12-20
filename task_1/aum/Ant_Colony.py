import numpy as np
import math
import csv
import time


class AnyColony(object):
    def __init__(self, height, width, decayRate, numberOfAnts, pheromoneWeighting, timeWeighting, cutOffPoint):
        self.decayRate = decayRate  # rate at which the pheremones vaporise
        self.numberOfAnts = numberOfAnts  # the number of ants to be used

        # Values used to prioritise either pheromone deposits or time taken on squares
        self.pheromoneWeighting = pheromoneWeighting
        self.timeWeighting = timeWeighting

        # Grid
        self.height = height  # height of grid
        self.width = width  # width of grid
        # setup a grid with random numbers 0,9
        self.grid = np.random.randint(0, 10, size=(height, width))
        # will store the pheromone value in correspondence to position in the grid # initialise a grid with 0 of size height x width
        self.pheromoneDeposits = np.full((height, width), 1)

        # Start and end points for the ants to reach
        self.startIndex = [0, 0]
        self.endIndex = [height - 1, width - 1]

        # Dictionary that stores the shortest path
        self.shortestPath = {"generation": 0, "length": 0, "path": []}

        self.generationToCompareTo = {"generation": 0, "length": 0, "path": []}
        self.toBreakCycle = False
        self.cutOffPoint = cutOffPoint
        self.currentPoint = 0

        #### TESTING ####
        # self.generateFixedGrid()

    # TEST CASE
    def generateFixedGrid(self):
        self.grid = np.array([
            [1, 4, 7, 2],
            [3, 6, 5, 3],
            [1, 2, 2, 1],
            [8, 6, 9, 1]
        ])
        # will store the pheromone value in correspondence to position in the grid # initialise a grid with 0 of size height x width
        self.pheromoneDeposits = np.full((4, 4), 1)
        self.width = 4
        self.height = 4
        self.endIndex = [3, 3]

    # calculate the score of a Square
    def calculateSquareScore(self, x, y):
        # multiply the pheromone with 1/timeTakenOnTheGrid (multiply the scalars as well)
        print("\nCALCULATE SCORE:")
        print("Grid value: ", self.grid[x, y])
        print("Pheremone Deposit: ", self.pheromoneDeposits[x, y])
        score = (self.pheromoneDeposits[x, y] ** self.pheromoneWeighting) * (
                (1 / self.grid[x, y]) ** self.timeWeighting)
        if math.isinf(score):
            score = 0
        print(score)
        return score

    # deposit the appropriate amount of pheremones at the certain position
    def depositPheromones(self, visitedSquares):
        # self.pheromoneDeposits[x, y] = 1 / self.grid[x, y]
        pathLength = 0
        for square in visitedSquares:
            pathLength += self.grid[square[0], square[1]]
        print("Path Length: ", pathLength)
        pheromoneAmount = 15 / (pathLength / len(visitedSquares))
        for square in visitedSquares:
            self.pheromoneDeposits[square[0], square[1]] += pheromoneAmount
            print("Pheremone Square = ", self.pheromoneDeposits[square[0], square[1]])

    # decay the pheromones that were placed in previous generations
    def decayPheromones(self):
        self.pheromoneDeposits = self.decayRate * self.pheromoneDeposits

    # Check if the current path is shorter than the previous path
    def checkPath(self, visitedSquares, generation):
        pathLength = 0
        for square in visitedSquares:
            pathLength += self.grid[square[0], square[1]]

        if pathLength < self.shortestPath["length"] or self.shortestPath["length"] == 0:
            self.shortestPath["length"] = pathLength
            self.shortestPath["path"] = visitedSquares
            self.shortestPath["generation"] = generation

    # Will break the cycle earlier if no change happens over cutOffPoint number of generations
    def checkBreakCycle(self, generation):
        if self.shortestPath["length"] == self.generationToCompareTo["length"] and self.generationToCompareTo["length"] != 0:
            if self.shortestPath["path"] == self.generationToCompareTo["path"]:
                self.currentPoint += 1
                if self.currentPoint == self.cutOffPoint:
                    self.toBreakCycle == True
            else:
                self.currentPoint == 0
                self.generationToCompareTo["length"] = self.shortestPath["length"]
                self.generationToCompareTo["path"] = self.shortestPath["path"]
                self.generationToCompareTo["generation"] = generation

    def run(self):

        print(self.grid)
        print(self.pheromoneDeposits)
        # iteratively go through every generation
        for i in range(self.numberOfAnts):
            currentPosition = self.startIndex
            visitedSquares = []  # the squares this and has visited

            # find available squares
            # find probability on each of them
            # move to one based on its probability (dont backtrack/unless reaching a dead end)
            # record the square it has gone too (needed to add pheromone values)
            # REPEAT until it reaches the end index
            #

            ########### HAVE NOT FIXED YET ##################
            if self.toBreakCycle:
                print()
                print("Ended Prematurally as saw no improvement.")
                print()
                break

            hasReachedTheEnd = False
            # loop until the ant has reached the end 
            while not hasReachedTheEnd:
                print(self.grid)

                print("\nCurrent Square: ", currentPosition)
                # store coordinates of the available squares
                availableSquares = [[currentPosition[0] + 1, currentPosition[1]],
                                    [currentPosition[0] - 1, currentPosition[1]], [
                                        currentPosition[0], currentPosition[1] + 1],
                                    [currentPosition[0], currentPosition[1] - 1]]

                # Remove squares out of bound
                tempSquares = []
                for square in availableSquares:
                    if (
                            not (square[0] < 0 or square[0] > self.width - 1 or square[1] < 0 or square[
                                1] > self.height - 1)):
                        tempSquares.append(square)
                availableSquares = tempSquares

                # Remove squares in visited
                # for i in range(len(visitedSquares)-1):

                #     availableSquares.pop(i)
                for square in visitedSquares:
                    if (square in availableSquares):
                        availableSquares.remove(square)

                print("Available Squares: ", availableSquares)

                # Calculate the square score
                squareScore = []
                for square in availableSquares:
                    # print("DEBUG\nAvailable Squares:" , availableSquares, "\nSquare:", square, "\n",)
                    if (square[0] == self.endIndex[0] and square[1] == self.endIndex[1]):
                        squareScore.append(10000)
                    else:
                        squareScore.append(
                            self.calculateSquareScore(square[0], square[1]))

                print("Square Score: ", squareScore)

                # Get the probabilities of each square
                probabilities = []
                for score in squareScore:
                    probabilities.append(score / len(squareScore))

                # the list of probabilities for each square
                print("Probability: ", probabilities)

                toChoose = -1  # which square to chose based on position int the availableSquares array
                probAdditive = 0
                randNo = np.random.uniform(0, np.sum(probabilities))

                # Calculate  which square to chose based on the probability.
                for probability in probabilities:
                    toChoose += 1  # Which square to choose
                    if probability + probAdditive < randNo:
                        break  # break out of the loop as on has been chosen
                    probAdditive += probability  # add to the additive so that it can compare properly

                print("Chosen: ", toChoose)  # index of the chosen square

                # if it has nowhere to go then move onto the next ant
                if toChoose == -1:
                    print("\n******************\nANT ", i + 1, " Destroyed \n*****************")
                    print("Visited Squares")
                    for square in visitedSquares:
                        print(square)
                    break

                visitedSquares.append(currentPosition)
                currentPosition = availableSquares[toChoose]
                if (currentPosition[0] == self.endIndex[0] and currentPosition[1] == self.endIndex[1]):
                    print("\n******************\nANT ", i + 1, " Made it \n*****************")
                    print("Visited Squares")
                    for square in visitedSquares:
                        print(square)
                    hasReachedTheEnd = True
                    visitedSquares.append(currentPosition)
                    self.depositPheromones(visitedSquares)
                    self.checkPath(visitedSquares, i)
                    self.checkBreakCycle(i)

                print("Pheremones")
                print(self.pheromoneDeposits)
                print()
            self.decayPheromones()
        print("\n___________________________")
        print("Shortest Path")
        print(self.shortestPath)
        print("___________________________")


startTimeSeconds = time.time()  # log the current time as of starting
# Call the ant colony
# height, width, decayRate, numberOfAnts, pheromoneWeighting, timeWeighting, cutOffPoint
antColony = AnyColony(50, 50, 0.7, 1000, 1, 1, 10)
antColony.run()
endTimeSeconds = time.time()  # log the time as of ending
totalTimeSeconds = endTimeSeconds - startTimeSeconds  # calculate total time
with open('task1_performance.csv', mode='a') as file:
    csvWriter = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    if antColony.shortestPath['length'] == 0:
        antColony.shortestPath['length'] = -1
    csvWriter.writerow(['ant-colony', antColony.height, antColony.width, antColony.shortestPath['length'], totalTimeSeconds, antColony.numberOfAnts])

# # Arguments
# decayRate = 0 # rate at which the pheremones vaporise
# numberOfAnts = 10 #the number of ants used in
#
# ## Values used to prioritise either pheromone deposits or time taken on squares
# pheromoneWeighting = 1
# distanceWeighting = 1
#
#
# ## Grid
# height = 10
# width = 10
# grid = np.random.randint(0,9,size=(height,width))
# pheromoneDeposits = np.full((height,width), 0)
#
# # Start and end points
# startIndex = [0,0]
# endIndex = [height-1, width-1]
#
# print(grid) # display the grid
# print(pheromoneDeposits) # will be filled with 0s as of now
#
# def calculateCityScore(x, y):
#     global pheromoneDeposits, pheromoneWeighting, grid, distance, distanceWeighting
#     return (pheromoneDeposits[x,y] * pheromoneWeighting) * ((1/grid[x,y])*distanceWeighting)
#
# def depositPheromones(x,y):
#     global pheromoneDeposits
#     pheromoneDeposits[x,y] = 1/grid[x,y]
#
# def decayPheromones():
#     global pheromoneDeposits
#     pheromoneDeposits= decayRate*pheromoneDeposits
