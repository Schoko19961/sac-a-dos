from cProfile import label
from bag import Bag
from history import History
from object import Object
from parametres import Parametres
from population import Population
import matplotlib.pyplot as plt
# Generate potential objects for the bag
objects = [Object() for _ in range(Parametres.NB_OBJ)]
for object in objects:
    print(object)
bags = [Bag(objects) for _ in range(Parametres.POPULATION_SIZE)]
population = Population(bags)
population.run()

history = [History(genome) for genome in population.history]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))
ax1.plot(list(map(lambda x: x.weight, history)), label='Weight')
ax1.axhline(y=Parametres.BAG_WEIGHT_MAX, linestyle='dashed', label='Max Weight')
ax1.plot(list(map(lambda x: x.value, history)), label='Value')
ax1.plot(list(map(lambda x: x.fitness, history)), label='Fitness')
ax1.legend()
ax2.plot(list(map(lambda x: x.ratio, history)), label='Value/Weight Ratio')
ax2.legend(loc="upper left")
ax3 = ax2.twinx()
ax3.plot(list(map(lambda x: x.items, history)), label='Items', color = 'tab:red')
ax3.legend(loc="upper right")
fig.tight_layout()
plt.savefig("img/plots/eval4.png")
