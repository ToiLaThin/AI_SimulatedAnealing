# %%
from matplotlib import pyplot as plt
import matplotlib
import numpy as np
import random
import math
from matplotlib.animation import FuncAnimation

x_lst = np.arange(0, 5, 0.1)
y_lst = []
curr_node = random.randint(0, len(x_lst)-1)
y = -2
for i in range(0, len(x_lst)):
    p = random.random()
    if p > 0.5:
        y = y + 2
    else:
        y = y - 2
    y_lst.append(y)


def schedule(t, k=20, lam=0.005, limit=1000):
    """One possible schedule function for simulated annealing"""
    return (k * np.exp(-lam * t) if t < limit else 0)

# node la gia tri idx trong x_lst


def expand(node):

    if node - 1 >= 0 and node + 1 <= len(x_lst)-1:
        return [node-1, node+1]
    else:
        return []


def value(node):
    return y_lst[node]


%matplotlib qt
fig, ax = plt.subplots()
ax.set_xlim(0, 5)
ax.set_ylim(-30, 30)


def animate(i):
    global curr_node
    ax.clear()
    ax.set_ylabel("Objective function")
    ax.set_title("Find Lowest point using simulted annealing")

    T = schedule(i)
    children = expand(curr_node)
    if len(children) > 0:
        id = random.randint(0, 1)
        next_node = children[id]
    else:
        next_node = random.randint(0, len(x_lst)-1)

    deltaE = value(curr_node) - value(next_node)
    if deltaE > 0:
        curr_node = next_node
    else:
        if math.e ** (float(deltaE)/T) > 0.5:
            curr_node = next_node

    ax.plot(x_lst, y_lst, color='b')
    ax.plot(x_lst[curr_node], y_lst[curr_node], marker='o',
            markerfacecolor='red', markeredgecolor='red', ms=10)
    return ax,


anim = FuncAnimation(fig, animate, frames=np.arange(
    1, 1000, 1), repeat=False, interval=50)


# %%
