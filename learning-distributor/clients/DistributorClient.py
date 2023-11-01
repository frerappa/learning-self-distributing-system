from models import UCB, BaseBanditModel
import requests


class DistributorClient:
    base_url = "http://localhost"
    base_port = 3500

    def __init__(self, type: str):
        self.model: BaseBanditModel = None
        self.model_type = type

    def _calculate_reward(self, average_response_time: float) -> float:
        return 100 / average_response_time

    def init_model(self):
        if self.model_type == "UCB":
            response = requests.get("{}:{}/ucb/init".format(base_url, base_port))
            # call api
            self.model: UCB = UCB(10)  # todo change
        else:
            return

    def update_reward(self):
        if self.model_type == "UCB":
            response = requests.get("{}:{}/ucb/perception-data".format(base_url, base_port))
            # should return current index and avg response time
            # call api
            self.model.update(
                10,  # action
                10.0  # reward
            )
        else:
            return

    def choose_index(self):
        if self.model_type == "UCB":
            next_composition = self.model.choose_composition_index()

            requests.post("{}:{}/ucb/composition".format(base_url, base_port), data=str(next_composition))

        else:
            return
