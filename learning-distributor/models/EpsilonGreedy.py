import numpy as np
# from mab import algs
# import numpy_ml

from models.BaseBanditModel import *


class EpsilonGreedy(BaseBanditModel):
    def __init__(self, epsilon: float, n: int):
        np.random.seed(1010)
        self.n = n
        self.epsilon = epsilon
        self.times_chosen = np.zeros(n)
        self.sum = np.zeros(n)

    def choose_composition_index(self) -> int:
        if np.random.random(size=1) > self.epsilon:
            return np.argmax(self.sum / self.times_chosen)
        else:
            return np.random.randint(self.n, size=1)

    def update(self, action: int, reward: float) -> None:
        self.sum[action] += reward
        self.times_chosen[action] += 1
