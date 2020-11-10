import numpy as np

class AnyColony(object):
    def __init__(self, height, width, decayRate, numberOfAnts, pheromoneWeighting, timeWeighting):
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
        self.pheromoneDeposits = np.full((height, width), 0)

        # Start and end points for the ants to reach
        self.startIndex = [0, 0]
        self.endIndex = [height-1, width-1]

        #### TESTING ####
        self.generateFixedGrid()

    # TEST CASE
    def generateFixedGrid(self):
        self.grid = np.array([
            [0, 4, 7, 2],
            [3, 6, 5, 3],
            [1, 2, 2, 1],
            [8, 6, 9, 0]
        ])
        # will store the pheromone value in correspondence to position in the grid # initialise a grid with 0 of size height x width
        self.pheromoneDeposits = np.full((4, 4), 0)

    # calculate the score of a Square
    def calculateSquareScore(self, x, y):
        # multiply the pheromone with 1/timeTakenOnTheGrid (multiply the scalars as well)
        return (self.pheromoneDeposits[x, y] * self.pheromoneWeighting) * ((1 / self.grid[x, y])*self.timeWeighting)

    # deposit the appropriate amount of pheremones at the certain position
    def depositPheromones(self, x, y):
        self.pheromoneDeposits[x, y] = 1 / self.grid[x, y]

    # decay the pheromones that were placed in previous generations
    def decayPheromones(self):
        self.pheromoneDeposits = self.decayRate * self.pheromoneDeposits

    def run(self):

        print(self.grid)
        print(self.pheromoneDeposits)

        # iteratively go through every generation
        for i in range(self.numberOfAnts):
            currentPosition = self.startIndex

            # find available squares
            # find probability on each of them
            # move to one based on its probability (dont backtrack/unless reaching a dead end)
            # record the square it has gone too (needed to add pheromone values)
            # REPEAT until it reaches the end index
            #
            print(i)


antColony = AnyColony(10, 10, 1, 10, 1, 1)
antColony.run()

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
