import torchvision
import torch
from torchvision import transforms, datasets
import torch.nn as nn
import torch.nn.functional as F
from sklearn.datasets import load_digits

# import dataframe
df = load_digits()

print(df)
