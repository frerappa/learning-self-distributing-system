import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    data = np.loadtxt("out.txt", dtype=float)
    plt.plot(data[data])
    plt.show()
