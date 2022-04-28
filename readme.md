# Sac a dos

# Le probleme
Une personne part en randonnée et emporte son sac à dos avec lui. Pour son voyage, il souhaite mettre quelques objets dans son sac à dos, mais il n'est pas assez fort pour tous les emballer, il doit donc limiter le poids.
Pour décider quels objets mettre dans son sac à dos, il a donné une valeur à chacun d'entre eux. Il essaie d'emporter la plus grande valeur sans dépasser la limite de poids.

# Les objets nécessaire
## Objet
- Un objet a une valeur et un poids. 
- Les objets sont invariable pendant tous les calculs pour le meilleur resultats.
## Sac à dos
- Le sac à dos contient des objets. 
- Il est possible de changer les objets dedans.
- Le sac à dos a un poids total qui est la somme de tous les objets dedans
- Le sac à dos a une valeur total qui est la somme de tous les objets dedans
- Le sac à un limite de poids qui est invariable.

# Approche de la solution
Le but de cette tâche est de maximiser la valeur du sac à dos en restant sous le limit du poids du sac à dos.

## Génétique
On resoudre ce problème avec un algrorithme de génétique.
Nous créons plusieurs sac à dos qui contiennent des objets par hazard.
### Génome
Le génome contient l'information sur quels objets sont dans le sac a dos. Donc tous les sac à dos ont un génome.

Il y deux possibilités comment on peut garder cet information dans un génome.
1. Le génome contient tout les objets et l'ordre des objet est important pour déterminer quels objets sont dans le sac. (Tous les objets jusqu'à ce que le sac à dos soit trop lourd.)
2. Le génome contient l'information pour tous les objets si l'objet est dans le sac ou pas. (Si le sac est trop lourd, il a une valeur de 0)

Le premier approche est inférieur, parce qu' il est impossible d'utiliser le principe de mère et père, juste la Mytose. C'est parce que si on melange les objets des deux sac à dos, on risque de dubliquer certains objets et de supprimer des autres.

Cet probleme n'existe pas dans le deuxième approche, parce que là, juste l'information si on objet est dans le sac a dos ou pas est changée.

### Fonctionne d'évaluation
Encore une fois il y a plusieurs possibilites pour la réalisation de cette fonctionne:
1. Les valeurs des objets sont ajoutéss et les poids sont supprimés
2. On utilise la rélation entre valeur et poids pour rapidement trouver les objets les plus efficace.
3. On utiliste juste les valeurs, mais si le sac est trop lourd, il a une valeur négative ou 0.