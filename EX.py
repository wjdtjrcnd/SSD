import torch
import numpy as np

## -- creating a tensor object
x = torch.tensor(np.arange(15).reshape(3, 5))
y = torch.tensor(np.zeros([3,5,5]))
x_dot = x.unsqueeze(x.dim()).expand_as(y)

print(x)
print(x_dot)