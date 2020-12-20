# IN3063_Maths_for_AI

## Team - Aum Patel (ACZG8967) & Johannes Heidecke (ACZG146)

Task 1 has been seperated into respective folders for both team members.

The python files use python3 with the appropriate libraries installed for the respective tasks (please check the import statements for the libraries)

All the work can be found in the Jupyter Notebooks of each task. The visualizations can be found in the visualization notebooks and in the visualization folder.

## Abstract

### Task 1: 25 marks
The first task tests your Python skills. You need to develop a simple game consisting of a rectangular grid (of size height x width ) where each cell has a random integer value between 0 and 9. An agent starts at the upper-left corner of the grid and must reach the lower-right corner of the grid as fast as possible.

You can implement one of the two (or both, for no extra point) game modes: 

- The time spent on a cell is the number on this cell
- The time spent on a cell is the absolute of the difference between the previous cell the agent was on and the current cell it is on

In order to solve this problem, you will provide 3 algorithms: 

- A first baseline of your choosing. E.g. it can be any search algorithm, or an algorithm using heuristics. It doesn’t have to perform fast or well, but should be better than random movements. 
- Dijkstra's algorithm 
- Ant colony optimization algorithm

You should describe the algorithms and compare them. Are they always solving the problem? How long do they take depending on the size of the maze?

### Task 2: 50 Marks

The second task is about classifying handwritten digits. We will use the MNIST dataset for training and testing.

The point of this task is to develop a multi-layer neural network for classification using mostly Numpy: 

- Implement sigmoid and relu layers (with forward and backward pass) 
- Implement a softmax output layer 
- Implement a fully parameterizable neural network (number and types of layers, number of units) 
- Implement an optimizer (e.g. SGD or Adam) and a stopping criterion of your choosing 
- Train your Neural Network using backpropagation.

Evaluate different neural network architectures and compare your different results. You can also compare with the results presented in http://yann.lecun.com/exdb/mnist/

### Task 3: 25 Marks

The third task is about comparing your results with architectures developed using PyTorch.

Compare the results obtained in Task 2 to the results obtained using the same architectures implemented in PyTorch.

Then, propose improvements and new architectures that make use of more advanced methods (e.g. Convolutional Neural Networks, dropout, …).

Compare the results.

Finally, present the confusion matrix of your best model.

### Task 4 : 20 Marks

For task four, we have decided to evaluate the performance of the different neural network libraries available in Python. The libraries that will be investigating are PyTorch and Keras. In the lecture 9, it was mentioned that it would be best to master one library and be sufficient in the others. To make the decision which one to choose we decided to evaluate their performances.