import time
from clients.DistributorClient import DistributorClient

OBSERVATION_WINDOW = 7.5  # in seconds

if __name__ == '__main__':
    client = DistributorClient("UCB")
    client.init_model()

    while True:
        time.sleep(OBSERVATION_WINDOW)
        client.update_reward()
        client.choose_index()