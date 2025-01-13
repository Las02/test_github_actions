import glob
import os

import matplotlib.pyplot as plt
import torch
from torch import logit, nn

# %load_ext autoreload
# %autoreload 2


class MyAwesomeModel(nn.Module):
    """My awesome model."""

    def __init__(self) -> None:
        super().__init__()
        self.seq = nn.Sequential(
            nn.Flatten(),
            nn.Linear(784, 128),
            nn.ReLU(),
            nn.Linear(128, 60),
            nn.ReLU(),
            nn.Linear(60, 10),
            nn.ReLU(),
        )

    def forward(self, x):
        x = self.seq(x)
        x = nn.LogSoftmax(dim=1)(x)
        return x
