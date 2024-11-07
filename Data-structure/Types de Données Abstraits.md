# Types de Données Abstraits (ADT)

Les **types de données abstraits** (Abstract Data Types ou ADT) sont des modèles théoriques de structures de données qui définissent des opérations logiques sur les données sans spécifier leur implémentation concrète. En d'autres termes, un ADT se concentre sur **ce que** les opérations font, plutôt que sur **comment** elles sont réalisées.

Les ADT sont utilisés pour organiser et manipuler les données dans les algorithmes de manière structurée et modulaire. Voici quelques types de données abstraits courants :

## 1. Pile (Stack)

Une **pile** est un ADT qui suit le principe LIFO (Last In, First Out). Cela signifie que le dernier élément ajouté est le premier à être retiré.

- **Opérations principales** :
  - `push` : ajoute un élément au sommet de la pile.
  - `pop` : retire l'élément au sommet de la pile.
  - `peek` : consulte l'élément au sommet sans le retirer.

Les piles sont souvent utilisées pour les opérations de retour arrière (undo) ou pour gérer les appels de fonctions en récursion.

## 2. File (Queue)

Une **file** est un ADT qui suit le principe FIFO (First In, First Out). Le premier élément ajouté est le premier à être retiré.

- **Opérations principales** :
  - `enqueue` : ajoute un élément à la fin de la file.
  - `dequeue` : retire l'élément en tête de la file.
  - `front` : consulte l'élément en tête sans le retirer.

Les files sont couramment utilisées dans la gestion des tâches en attente, comme les files d'attente dans les systèmes d'impression.

## 3. Liste (List)

Une **liste** est un ADT qui représente une séquence ordonnée d'éléments. Les éléments peuvent être ajoutés, retirés, ou accédés par leur position dans la séquence.

- **Opérations principales** :
  - `insert` : ajoute un élément à une position spécifique.
  - `remove` : retire un élément d'une position spécifique.
  - `get` : accède à un élément par son index.

Les listes sont très utilisées pour stocker des collections d'éléments dans un ordre particulier.

## 4. Dictionnaire (Map ou Hash Map)

Un **dictionnaire** est un ADT qui stocke des paires clé-valeur, où chaque clé est unique et associée à une valeur.

- **Opérations principales** :
  - `put` : ajoute ou met à jour une valeur pour une clé.
  - `get` : récupère la valeur associée à une clé.
  - `remove` : supprime une paire clé-valeur.

Les dictionnaires sont utilisés pour des recherches rapides d’éléments par clé, comme dans les annuaires téléphoniques ou les bases de données.

## 5. Ensemble (Set)

Un **ensemble** est un ADT qui stocke des éléments uniques sans ordre spécifique.

- **Opérations principales** :
  - `add` : ajoute un élément.
  - `remove` : supprime un élément.
  - `contains` : vérifie si un élément est présent.

Les ensembles sont utiles pour gérer des collections d’éléments uniques et effectuer des opérations ensemblistes, comme l'union et l'intersection.

## 6. Arbre (Tree)

Un **arbre** est un ADT hiérarchique où chaque élément (appelé nœud) a un parent unique et potentiellement plusieurs enfants.

- **Opérations principales** :
  - `insert` : ajoute un nœud à une position spécifique.
  - `delete` : supprime un nœud.
  - `traverse` : parcourt l'arbre dans un ordre particulier (préordre, en ordre, postordre).

Les arbres sont utilisés pour représenter des hiérarchies, comme les systèmes de fichiers ou les bases de données.

## Conclusion

Les types de données abstraits permettent de structurer et de manipuler les données de manière flexible et cohérente, sans se préoccuper de leur implémentation sous-jacente. Choisir le bon ADT pour une application donnée est essentiel pour optimiser les performances et rendre le code plus lisible et maintenable.
