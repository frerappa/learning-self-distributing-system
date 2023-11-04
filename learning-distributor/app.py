import time
from clients.DistributorClient import DistributorClient

OBSERVATION_WINDOW = 7.5  # in seconds
MODEL = "UCB"

if __name__ == '__main__':
    print(f"Server started with model {MODEL} and observation window {OBSERVATION_WINDOW} seconds")
    client = DistributorClient(MODEL)
    client.init_model()

    while True:
        time.sleep(OBSERVATION_WINDOW)
        client.update_reward()
        client.choose_index()