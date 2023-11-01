from flask import Flask

from clients.models.UCBClient import ucb1_routes
from clients.models.EpsilonGreedyClient import epsilon_greedy_routes

app = Flask(__name__)
app.register_blueprint(ucb1_routes)
app.register_blueprint(epsilon_greedy_routes)

if __name__ == '__main__':
    app.run(port=3000)

# http://localhost:3500/