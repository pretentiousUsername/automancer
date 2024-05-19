from automancer import CellularAutomata, game_of_life
from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np
import os

initial_state = np.load("state.npy")
game = CellularAutomata((20, 20))
game.add_neighborhood(shape = 'm', size = 1)
game.add_rule(game_of_life)
game.set_state(initial_state)

energy = []
time = range(0, 200)
for t in time:
    game.evaluate_rules()
    energy.append(game.energy())

plt.plot(energy)
plt.xlabel("generation")
plt.ylabel("number of living cells")
plt.savefig("energy.svg")
