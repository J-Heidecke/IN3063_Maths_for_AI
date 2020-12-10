import torchvision
import torch
from torchvision import transforms, datasets
import torch.nn as nn
import torch.nn.functional as F
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

# import dataframe # reduced version of the MNIST dataset
digits = load_digits()
df = torchvision.datasets.MNIST
# print(df.train_data)
trainset = datasets.MNIST(root='./data', train=True, download=True, transform=None)
testset = datasets.MNIST(root='./data', train=False, download=True, transform=None)


# print(digits.DESCR)
# print(digits.keys())

plt.imshow(digits.images[1010], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()
plt.imshow(trainset.data[1011], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()