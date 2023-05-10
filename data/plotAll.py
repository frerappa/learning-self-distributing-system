import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    plt.yscale("log")
    dataLocal = np.loadtxt("local.txt", dtype=float)
    plt.plot(dataLocal)

    shard = np.loadtxt("shard.txt", dtype=float)
    plt.plot(shard[shard < 10000])

    propagate = np.loadtxt("propagate.txt", dtype=float)
    plt.plot(propagate)

    # ucb = np.loadtxt("ucb-remote.txt", dtype=float)
    # plt.plot(ucb)


    plt.title("Configuração readn-writen")
    plt.legend(["Local", "Sharding", "Propagate"])
    plt.xlabel("Número de requisições")
    plt.ylabel("Tempo de resposta (ms)")
    plt.grid()
    
    plt.show()
