from random import randint, choices
import numpy as np

da = []
da2 = []
arange = list(np.arange(1, 100, 0.5))
arange2 = list(np.arange(1, 100))
epochs = 1000
for i in range(epochs):
    if randint(1,2) == 1: choice = choices(arange, k=2); da2.append(0)
    else: choice = choices(arange2, k=2); da2.append(1)
    da.append(choice)

print(da)
print("\n\n")
print(da2)