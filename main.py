from cProfile import label
from bag import Bag
from history import History
from object import Object
from parametres import Parametres
from population import Population
import matplotlib.pyplot as plt

# Generation des objets pour le sac à dos.
objects = [Object() for _ in range(Parametres.NB_OBJ)]
for object in objects:
    print(object)
# Generation des sacs à dos.
bags = [Bag(objects) for _ in range(Parametres.POPULATION_SIZE)]
population = Population(bags)
# Lance l'algorithme génétique.
population.run()

# Creation de l'histoire basé sur les meilleurs genomes dans la population
history = [History(genome) for genome in population.history]

# Creation du diagram
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))
# Creation de la partie gauche avec: ["Weight", "Max Weight", "Value", "Fitness"]
ax1.plot(list(map(lambda x: x.weight, history)), label='Weight')
ax1.axhline(y=Parametres.BAG_WEIGHT_MAX, linestyle='dashed', label='Max Weight')
ax1.plot(list(map(lambda x: x.value, history)), label='Value')
ax1.plot(list(map(lambda x: x.fitness, history)), label='Fitness')
ax1.legend()
# Creation de la partie droite avec: ["Value/Weight Ratio", "Items"]
ax2.plot(list(map(lambda x: x.ratio, history)), label='Value/Weight Ratio')
ax2.legend(loc="upper left")
# Creation d'un deuxième axe à droite.
ax3 = ax2.twinx()
ax3.plot(list(map(lambda x: x.items, history)), label='Items', color = 'tab:red')
ax3.legend(loc="upper right")
fig.tight_layout()
plt.show()
