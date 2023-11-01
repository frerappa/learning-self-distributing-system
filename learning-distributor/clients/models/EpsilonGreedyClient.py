from flask import Blueprint, request
from models.EpsilonGreedy import *
from multiprocessing import Value
import pickle


base_path = "epsilon-greedy"
epsilon_greedy_routes = Blueprint(base_path, __name__)
FILE = "obj.txt"


@epsilon_greedy_routes.route(f"/{base_path}/init", methods=["POST"])
def init_method():
    epsilon, arms = request.data.decode('utf-8').split("|")
    greedy_model: EpsilonGreedy = EpsilonGreedy(float(epsilon), int(arms))
    file = open(FILE, 'wb')
    pickle.dump(greedy_model, file)
    file.close()
    print("Initializing Epsilon-Greedy model with {} arms and eps={}".format(arms, epsilon))
    return "ok"


@epsilon_greedy_routes.route(f"/{base_path}/reward", methods=["POST"])
def reward_action():
    file = open(FILE, 'rb')
    greedy_model: EpsilonGreedy = pickle.load(file)
    if not greedy_model:
        raise Exception("Model has not been instantiated")
    action, reward = request.data.decode('utf-8').split("|")
    print("Reward value {} for action {}".format(reward, action))
    greedy_model.update(int(action), float(reward))
    file = open(FILE, 'wb')
    pickle.dump(greedy_model, file)
    file.close()
    return "ok"


@epsilon_greedy_routes.route(f"/{base_path}/composition", methods=["GET"])
def get_composition():
    file = open(FILE, 'rb')
    greedy_model: EpsilonGreedy = pickle.load(file)
    if not greedy_model:
        raise Exception("Model has not been instantiated")
    idx = greedy_model.choose_composition_index()
    file.close()
    print("Pulling arm {}".format(idx))
    return str(idx)



