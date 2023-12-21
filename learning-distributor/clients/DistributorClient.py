from models.UCB import *
from models.BaseBanditModel import *
import requests


class DistributorClient:
    base_url = "http://localhost"
    base_port = 3500

    def __init__(self, type: str):
        self.model: BaseBanditModel = None
        self.model_type = type
        self.should_reconfigure: bool = True

    def _calculate_reward(self, average_response_time: float) -> float:
        return 100 / average_response_time

    def init_model(self):
        if self.model_type == "UCB":
            response = requests.get(f"{DistributorClient.base_url}:{DistributorClient.base_port}/ucb/init")
            arms = int(response.content.decode('utf-8'))
            print(f"Initializing UCB1 model with {arms} arms")
            self.model: UCB = UCB(arms)  # todo change

    def update_reward(self):
        if self.model_type == "UCB":
            response = requests.get(f"{DistributorClient.base_url}:{DistributorClient.base_port}/ucb/perception-data")
            print(response.content)
            if (response.content.decode('utf-8') == "NOT FOUND"):
                self.should_reconfigure = False
                return
            self.should_reconfigure = True
            action, average_response_time = response.content.decode('utf-8').split("|")
            reward = self._calculate_reward(float(average_response_time))
            print(f"Reward value {reward} for action {action} with average response time {average_response_time}")
            self.model.update(
                int(action),
                reward
            )

    def choose_index(self):
        if self.model_type == "UCB":
            if not self.should_reconfigure:
                return

            next_composition = self.model.choose_composition_index()
            print(f"Pulling arm {next_composition}")
            requests.post(f"{DistributorClient.base_url}:{DistributorClient.base_port}/ucb/composition", data=str(next_composition))
