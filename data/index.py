import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    data = np.loadtxt("out.txt", dtype=float)
    plt.yscale("log")

    plt.plot(data)
    plt.show()
