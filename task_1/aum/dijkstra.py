import heapq
import numpy as np
import itertools
import time
import csv


class Element:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    # overriding a default method to check whether or not two elements are equal
    def __eq__(self, other):
        return self.value['position'] == other.value['position']

    # override the comparison operator
    def __lt__(self, other):
        return self.key < other.key


# parameters
height = 15
width = 15
start = [0, 0]
end = [height - 1, width - 1]

grid = np.random.randint(0, 10, size=(height, width))  # create grid

# initialise the queue as empty
q = []  # will store the position, cost, and prev
# counter = itertools.count()  # counter to use as a tie breaker when adding to a heap queue


def addToQueue(position, time, prev=np.inf, lookedAt=False):
    global q
    # heapq.heappush(q, (time, next(counter), {'position': position, 'time': time, 'prev': prev, 'lookedAt': lookedAt}))
    tempElement = Element(time, {'position': position, 'time': time, 'prev': prev, 'lookedAt': lookedAt})
    heapq.heappush(q, tempElement)


def getNeighbours(currentPosition):
    positions = []

    # Right
    x = currentPosition[0] + 1
    y = currentPosition[1]
    if height > x >= 0 and width > y >= 0:
        positions.append([x, y])

    # Left
    x = currentPosition[0] - 1
    if height > x >= 0 and width > y >= 0:
        positions.append([x, y])

    # Down
    x = currentPosition[0]
    y = currentPosition[1] + 1
    if height > x >= 0 and width > y >= 0:
        positions.append([x, y])

    # Up
    y = currentPosition[1] - 1
    if height > x >= 0 and width > y >= 0:
        positions.append([x, y])

    return positions


startTimeSeconds = time.time()  # log the current time as of starting

# add the start to the queue
addToQueue(position=start, time=0)
hasReachedTheEnd = False
finalNode = {}

while not hasReachedTheEnd:
    # get the current, which is the node to be checked now
    current = -1
    for e in q:
        current += 1
        # ignore positions that have already been looked at properly
        if not e.value['lookedAt']:
            break  # break out of this loop to prevent further searching

    if current == -1:
        print("ERROR: no elements in q")
        break

    if q[current].value['lookedAt']:
        print("ERROR: no new element found")

    # find the neighbours, then add them to the queue
    neighbours = getNeighbours(q[current].value['position'])

    for n in neighbours:

        # do a check to see if we have finished
        if n[0] == end[0] and n[1] == end[1]:
            hasReachedTheEnd = True
            addToQueue(n, grid[n[0], n[1]] + q[current].value['time'], prev=q[current].value['position'])
            finalNode = {'position': n, 'time': grid[n[0], n[1]] + q[current].value['time'], 'prev': q[current].value['position'], 'lookedAt': False}
            break
        else:

            # check if the position exists
            # if it doesn't exits
            if not Element(0, {'position': [n[0], n[1]]}) in q:
                # check the length
                addToQueue(n, grid[n[0], n[1]] + q[current].value['time'], prev=q[current].value['position'])
            else:
                for e in q:
                    # check if getting to the neighbour is faster from this node
                    if e.value['position'] == n:  # if the (position = n) as some times they will have identical keys as the key is time
                        if grid[n[0], n[1]] + q[current].value['time'] < e.value['time']:  # if the new one is less
                            addToQueue(n, grid[n[0], n[1]] + q[current].value['time'], prev=q[current].value['position'])
                        else:
                            break  # break out of this loop to prevent further searching
    # set the looked at to true for the current node
    q[current].value['lookedAt'] = True


# calculate the path
pathCalculated = False
path = [finalNode['position']]
prev = finalNode['prev']

dijkstraNotWork = False

counter = 0
while not pathCalculated and not dijkstraNotWork:
    counter += 1

    # break out and end the program as there is a bug that prevents dijkstra from reaching the start
    if counter % 10000 == 0:
        # print(path)
        print("please re-run the code")
        dijkstraNotWork = True

    for e in q:
        if e.value['position'] == prev:
            path.append(e.value['prev'])
            prev = e.value['prev']

    if prev == start:
        pathCalculated = True

if not dijkstraNotWork:
    path.reverse()

    endTimeSeconds = time.time()  # log the time as of ending
    totalTimeSeconds = endTimeSeconds - startTimeSeconds  # calculate total time
    print("final:", finalNode)  # time of path will be stored in this, but to get path I will have to traverse
    print("final path: ", path)
    print("shortest path length: ", finalNode['time'])
    print("total time taken (seconds):", totalTimeSeconds)
    with open('task1_performance.csv', mode='a') as file:
        csvWriter = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvWriter.writerow(['dijkstra', height, width, finalNode['time'], totalTimeSeconds, 1])

