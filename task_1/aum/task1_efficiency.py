# Created csv file for reading the efficiency
import matplotlib.pyplot as plt
import pandas as pd  # using pandas to read csv file to visualise the results

df = pd.read_csv("task1_performance.csv")

averages = []

encode = [1, 2, 3]
labels = ['ant-colony', 'baseline', 'dijkstra']
labelDict = {'ant-colony': 1, 'baseline': 2, 'dijkstra': 3}


def getAverage(algorithm, size):
    algoDf = df[df.algorithm == algorithm]  # get ant colony runs
    algoDf = algoDf[algoDf.height == size]  # get the 10x10 ones
    algoDfFailed = algoDf[algoDf['grid_time'] == -1].count()['algorithm']  # get the number of failed ant colonies
    algoDf = algoDf[algoDf.grid_time != -1]  # get rid of values where it did not reach
    encodedAlgo = -1
    for i in range(len(labels)):
        if labels[i] == algorithm:
            encodedAlgo = encode[i]
    averages.append({'algorithm': encodedAlgo, 'size': size, 'grid_time': algoDf['grid_time'].mean(), 'real_time': algoDf['real_time'].mean(), 'failed': algoDfFailed})


def plotAverage(y, filterAlgorithm='no'):
    toPlotX = []
    toPlotY = []

    # extracting grid time to plot
    for e in averages:
        print(e)
        if filterAlgorithm == 'no':
            toPlotX.append(e['algorithm'])
            toPlotY.append(e[y])
        else:
            if e['algorithm'] == labelDict[filterAlgorithm]:
                toPlotX.append(e['algorithm'])
                toPlotY.append(e[y])

    plt.bar(toPlotX, toPlotY)
    plt.xticks(encode, labels)

    plt.title('Average ' + y)

    if y == 'real_time':
        plt.ylabel('seconds')

    plt.show()


getAverage('ant-colony', 10)
getAverage('baseline', 10)
getAverage('dijkstra', 10)

plotAverage('grid_time')
plotAverage('real_time')
plotAverage('real_time', filterAlgorithm='baseline')
