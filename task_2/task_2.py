# # Import limited libraries
# from sklearn.datasets import load_digits
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
#
# # Load MNIST Dataset
# df = load_digits()
# # Divorce data and target
# X = df.data
# y = df.target
#
# # Splitting Dataset - Inspiration taken from Lab 04
# ratio = 0.75
# length = len(X)
#
# X_train = X[:int(length * ratio)]
# X_test = X[int(length * ratio):]
# y_train = y[:(length - int(length * ratio))]
# y_test = y[(length - int(length * ratio)):]
#
# # Normalize Dataset
# X_train = X_train / 255.0
# X_test = X_test / 255.0
#
#
# # Activation functions
#
# # Sigmoid function
# def sigmoid_forwards(inputs):
#     return 1 / (1 + np.exp(-inputs))
#
#
# # Derivative of Sigmoid (for backward propagation)
# def sigmoid_backwards(derivative, inputs):
#     sig = sigmoid_forwards(inputs)
#     return derivative * sig * (1 - sig)
#
#
# # ReLu function
# def relu_forward(inputs):
#     return np.maximum(0, inputs)
#
#
# # Derivative of ReLu
# def relu_backward(derivative, inputs):
#     derivative = np.array(derivative, copy=True)
#     derivative[inputs <= 0] = 0;
#     return derivative;
#
#
# # Softmax function for output
# def softmax_forward(self):
#     e = np.exp(self.inputs)
#     return e / e.sum()
#
#
# # Derivative of softmax
# def softmax_backward(derivative, inputs):
#     # soft = softmax(inputs)
#     soft = softmax_forward(inputs)
#     return derivative * soft * (1 - soft)
#
#
# # Cost function
# def get_cost(target, output):
#     m = target.shape[1]
#     cost = -1 / m * (np.dot(output, np.log(target).T) + np.dot(1 - output, np.log(1 - target).T))
#     return np.squeeze(cost)
#
#
# nn_architecture = [
#     {"input_dim": 2, "output_dim": 4, "activation": "relu"},
#     {"input_dim": 4, "output_dim": 6, "activation": "relu"},
#     {"input_dim": 6, "output_dim": 6, "activation": "relu"},
#     {"input_dim": 6, "output_dim": 4, "activation": "relu"},
#     {"input_dim": 4, "output_dim": 1, "activation": "sigmoid"},
# ]
#
# np.random.seed(0)
#
#
# class NeuralNetwork:
#
#     def __init__(self, nn_architecture):
#
#         self.memory = {}
#         self.nn_architecture = nn_architecture
#
#     def initialize(self):
#
#         for idx, layer in enumerate(self.nn_architecture):
#             layer_number = idx + 1
#             layer_input_size = layer["input_dim"]
#             layer_output_size = layer["output_dim"]
#
#             self.memory['Weight' + str(layer_number)] = 0.1 * np.random.randn(
#                 layer_output_size, layer_input_size)
#             self.memory['bias' + str(layer_number)] = 0.1 * np.random.randn(
#                 layer_output_size, 1)
#
#         # return memory
#
#     def forward(self, inputs, weights, biases, activation):
#
#         output_forward = np.dot(inputs, weights) + biases
#
#         ## HAVE NOT FILLED INPUT PARAMERTERS ##
#         if activation == 'sigmoid':
#             activation_function = sigmoid_forwards() #params
#         elif activation == 'relu':
#             activation_function = relu_forward()#params
#         elif activation == 'softmax':
#             activation_function = softmax_forward() #params
#         else:
#             raise Exception('Activation function not defined')
#
#         return activation_function(output_forward), output_forward
#
#     def forward_full(self, X, memory):
#         temp = {}
#         inputs_current = X
#
#         for idx, layer in enumerate(self.nn_architecture):
#             layer_number = idx + 1
#             inputs_previous = inputs_current
#
#             activation_function_current = layer['activation']
#             weight_current = memory['Weight' + str(layer_number)]
#             bias_current = memory['bias' + str(layer_number)]
#             output_forward, result_forward = self.forward(inputs_previous, weight_current, bias_current,
#                                                           activation_function_current)
#
#             temp['Output' + str(layer_number)] = output_forward
#             temp['Result' + str(layer_number)] = result_forward
#
#         return inputs_current, temp
#
#     def backward(self, inputs):
#         m = inputs.shape
#
#         if (activation == 'sigmoid'):
#             activation_function = Sigmoid_backward()
#         elif (activation == 'relu'):
#             activation_function = Relu_backward()
#         elif (activation == 'softmax'):
#             activation_function = Softmax_backward()
#         else:
#             raise Exception('Activation function not defined')
#
#         output_backwards = activation_function()
#         weight_backwards = np.dot().T / m
#         bias_backwards = np.sum() / m
#         resul_backwards
#
#     def full_backward(self, target, output, memory, temp, nn_architecture):
#
#         derived_values = {}
#
#         m = output.shape[1]
#         output = output.reshape(target.shape)
#         output_error_previous = np.divide(1 - output, 1 - target) - (np.divide(output, target)
#
#                                                                      for layer_number_previous, layer in reversed(list(enumerate(nn_architecture))):
#         layer_number_current = layer_number_previous + 1
#         activation_function = layer["activation"]
#
#         output_error_current = output_error_previous
#
#         outpt_previous = memory["Output" + str(layer_number_previous)]
#         result_current = memory["Result" + str(layer_number_current)]
#         weight_current = params_values["Weight" + str(layer_number_current)]
#         bias_current = params_values["bias" + str(layer_number_current)]
#
#         error = np.divide(1 - output, 1 - target) - (np.divide(output, target)
#
#     def update_weight(self):
#         pass;
#
#
#
# nn = NeuralNetwork(nn_architecture)
# nn.initialize()
# nn.full_forward(X_train)
#
#
#
# layers = init_layers(nn_architecture)
# print(layers)