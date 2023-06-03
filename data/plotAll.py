import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    plt.yscale("log")

    legend = []

    dataLocal = np.loadtxt("local.txt", dtype=float)
    plt.plot(dataLocal)
    legend.append("Local")

    shard = np.loadtxt("shard.txt", dtype=float)
    plt.plot(shard)
    legend.append("Sharding")


    propagate = np.loadtxt("propagate.txt", dtype=float)
    plt.plot(propagate)
    legend.append("Propagate")


    alternate = np.loadtxt("alternate.txt", dtype=float)
    plt.plot(alternate)
    legend.append("Alternate")

    ucb = np.loadtxt("UCB.txt", dtype=float)
    plt.plot(ucb)
    legend.append("Learning - UCB")


    plt.title("Configuração readn-writen")
    plt.legend(legend)
    plt.xlabel("Número de requisições")
    plt.ylabel("Tempo de resposta (ms)")
    plt.grid()
    
    plt.show()
