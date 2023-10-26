from flask import Blueprint, request
from models.UCB import *
from multiprocessing import Value
import pickle


base_path = "ucb1"
ucb1_routes = Blueprint(base_path, __name__)
FILE = "obj.pkl"


@ucb1_routes.route(f"/{base_path}/init", methods=["POST"])
def init_method():
    arms = int(request.data)
    ucb1_model: UCB = UCB(arms)
    file = open(FILE, 'wb')
    pickle.dump(ucb1_model, file)
    file.close()
    print("Initializing UCB1 model with {} arms".format(arms))
    return "ok"


@ucb1_routes.route(f"/{base_path}/reward", methods=["POST"])
def reward_action():
    file = open(FILE, 'rb')
    ucb1_model: UCB = pickle.load(file)
    if not ucb1_model:
        raise Exception("Model has not been instantiated")
    action, reward = request.data.decode('utf-8').split("|")
    print("Reward value {} for action {}".format(reward, action))
    ucb1_model.update(int(action), float(reward))
    file = open(FILE, 'wb')
    pickle.dump(ucb1_model, file)
    file.close()
    return "ok"


@ucb1_routes.route(f"/{base_path}/composition", methods=["GET"])
def get_composition():
    file = open(FILE, 'rb')
    ucb1_model: UCB = pickle.load(file)
    if not ucb1_model:
        raise Exception("Model has not been instantiated")
    idx = ucb1_model.choose_composition_index()
    file.close()
    print("Pulling arm {}".format(idx))
    return str(idx)



