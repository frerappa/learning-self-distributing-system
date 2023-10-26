import numpy as np
# from mab import algs
# import numpy_ml

from models.BaseBanditModel import *


class UCB(BaseBanditModel):
    def __init__(self, n: int):
        self.n = n
        self.iterations = 0
        self.times_chosen = np.zeros(n)
        self.sum = np.zeros(n)

    def choose_composition_index(self) -> int:
        indices = np.where(self.times_chosen == 0)[0]
        if len(indices) > 0:
            return indices[0]
        confidence_level = (self.sum / self.times_chosen) + np.sqrt((2 * np.log(self.iterations)) / (1 + self.times_chosen))
        return np.argmax(confidence_level)

    def update(self, action: int, reward: float) -> None:
        self.iterations += 1
        self.sum[action] += reward
        self.times_chosen[action] += 1
