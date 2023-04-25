import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    plt.yscale("log")
    dataLocal = np.loadtxt("local.txt", dtype=float)
    plt.plot(dataLocal)

    shard = np.loadtxt("shard.txt", dtype=float)
    plt.plot(shard)

    ucb = np.loadtxt("ucb-remote.txt", dtype=float)
    plt.plot(ucb)

    
    plt.show()
