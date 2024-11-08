## Discussion et Exemples de PQ (Files de Priorité)

### Qu'est-ce qu'une PQ (File de Priorité) ?

Une **file de priorité** est une structure de données où chaque élément a une priorité associée. Contrairement à une queue classique (FIFO), dans une file de priorité, les éléments sont retirés en fonction de leur priorité plutôt que de l'ordre d'arrivée. Les éléments avec une priorité plus élevée sont servis avant ceux avec une priorité plus faible.

Il existe deux types de files de priorité :

- **Min PQ** : La priorité la plus basse est servie en premier.
- **Max PQ** : La priorité la plus haute est servie en premier.

### Qu'est-ce qu'un Heap ?

Un **heap** est une structure de données en forme d'arbre binaire utilisé pour implémenter les files de priorité. Un heap peut être un **min-heap** ou un **max-heap** :

- **Min-heap** : Chaque nœud est inférieur ou égal à ses enfants, garantissant que l'élément avec la plus basse priorité est toujours à la racine.
- **Max-heap** : Chaque nœud est supérieur ou égal à ses enfants, garantissant que l'élément avec la plus haute priorité est toujours à la racine.

### Comment Choisir entre un Min-Heap et un Max-Heap ?

Le choix entre un **min-heap** et un **max-heap** dépend de la manière dont tu veux traiter les éléments prioritaires dans ton application :

- **Min-heap** :
  - Utilisé pour accéder rapidement à l'élément de **plus basse priorité**.
  - Cas d'utilisation : 
    - **Algorithmes de plus court chemin** (comme Dijkstra), où le nœud avec la distance la plus courte doit être exploré en premier.
    - **Planification de tâches avec des coûts** : Lorsque tu veux minimiser les coûts en traitant d'abord les tâches les moins coûteuses.
    - **Traitement d'événements** dans des calendriers ou des simulations, où les événements les plus proches dans le temps sont traités en premier.

- **Max-heap** :
  - Utilisé pour accéder rapidement à l'élément de **plus haute priorité**.
  - Cas d'utilisation :
    - **Classements** ou **scores** : Pour obtenir les valeurs les plus élevées en premier.
    - **Systèmes de priorisation** : Dans des systèmes en temps réel où les tâches les plus importantes doivent être traitées avant les autres.
    - **File d'attente d'urgence** : Par exemple, pour des files d'attente dans des hôpitaux, où les patients les plus critiques sont traités en premier.

- **Facilité d'inversion** : Si ton application nécessite parfois une min-heap et parfois une max-heap, tu peux utiliser une seule structure (par exemple, un min-heap) et inverser les priorités. Par exemple, en multipliant les priorités par -1 dans un min-heap, tu peux simuler un max-heap.

### Quand et Où Utiliser une PQ ?

Les files de priorité sont utilisées dans divers domaines en informatique, notamment :

- **Planification des tâches** dans les systèmes d'exploitation, où les processus avec des priorités plus élevées sont exécutés en premier.
- **Algorithmes de graphes**, comme l'algorithme de Dijkstra pour trouver le chemin le plus court, qui utilise une file de priorité pour sélectionner le prochain nœud à explorer.
- **Traitement d'événements** dans des simulations, où les événements doivent être traités en fonction de leur ordre de priorité.

### Comment Transformer une Min PQ en Max PQ ?

Pour transformer une **Min PQ** en **Max PQ**, il suffit d'inverser les priorités des éléments. Par exemple, on peut multiplier chaque priorité par -1, ce qui transforme les valeurs minimales en maximales et vice-versa. Alternativement, on peut utiliser une structure de max-heap pour la file de priorité.

### Analyse de Complexité

Les opérations dans une file de priorité basée sur un heap ont les complexités suivantes :

| Opération            | Complexité |
| -------------------- | ---------- |
| Insertion            | O(log n)   |
| Extraction (min/max) | O(log n)   |
| Accès au min/max     | O(1)       |

La structure de heap garantit que l'élément de plus haute (ou plus basse) priorité est accessible en temps constant, tandis que l'insertion et l'extraction nécessitent un temps logarithmique pour maintenir la propriété de l'arbre.

## Détails de l'Implémentation d'une File de Priorité avec un Heap Binaire

### Heap Sinking et Swimming (Aussi Appelé Sift Down et Sift Up)

- **Heap sinking (Sift Down)** : Utilisé lors de l'extraction de l'élément avec la priorité la plus haute (ou la plus basse). Cette opération descend un nœud dans le heap pour rétablir la propriété de min-heap ou max-heap.
- **Heap swimming (Sift Up)** : Utilisé lors de l'insertion d'un nouvel élément. Cette opération monte un nœud dans le heap pour maintenir la structure de priorité.

### Ajouter des Éléments dans une PQ

Lorsqu'un élément est ajouté à la file de priorité, il est d'abord placé à la fin du heap. Ensuite, l'opération **sift up** est effectuée pour le déplacer à sa position correcte en fonction de sa priorité.

### Retirer (Polling) des Éléments de la PQ

Lorsqu'on retire l'élément avec la priorité la plus haute (ou la plus basse) de la file de priorité, cet élément (la racine du heap) est remplacé par le dernier élément. Ensuite, l'opération **sift down** est effectuée pour restaurer la structure du heap.

## Implémentation en Code

Voici un exemple simple d'implémentation d'une file de priorité en Python en utilisant un min-heap avec le module `heapq` :

```python
import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    # Ajouter un élément dans la file de priorité
    def enqueue(self, priority, item):
        heapq.heappush(self.heap, (priority, item))
        print(f"Élément {item} avec priorité {priority} ajouté")

    # Retirer l'élément avec la priorité la plus basse (min-heap)
    def dequeue(self):
        if not self.is_empty():
            priority, item = heapq.heappop(self.heap)
            print(f"Élément {item} avec priorité {priority} retiré")
            return item
        else:
            print("La file de priorité est vide")
            return None

    # Consulter l'élément avec la priorité la plus basse sans le retirer
    def peek(self):
        if not self.is_empty():
            priority, item = self.heap[0]
            return item
        else:
            print("La file de priorité est vide")
            return None

    # Vérifier si la file de priorité est vide
    def is_empty(self):
        return len(self.heap) == 0

    # Afficher la file de priorité
    def display(self):
        print("État actuel de la file de priorité :", self.heap)

# Utilisation de la file de priorité
pq = PriorityQueue()
pq.enqueue(2, "Tâche moyenne")
pq.enqueue(1, "Tâche haute priorité")
pq.enqueue(3, "Tâche basse priorité")
pq.display()                  # Affiche l'état actuel du heap
print("Élément prioritaire :", pq.peek())  # Affiche la tâche de plus haute priorité
pq.dequeue()                  # Retire l'élément de plus haute priorité
pq.display()                  # Affiche l'état actuel après retrait
```

## Explication du code ##

- **enqueue** : Ajoute un élément avec une priorité donnée à la file de priorité.
- **dequeue** : Retire l'élément avec la priorité la plus basse (min-heap) de la file de priorité.
- **peek** : Consulte l'élément avec la priorité la plus basse sans le retirer.
- **is_empty** : Vérifie si la file de priorité est vide.
- **display** : Affiche l'état actuel de la file de priorité.

Ce code utilise le module `heapq` de Python pour implémenter un min-heap pour la file de priorité. Les éléments sont stockés sous forme de tuples `(priorité, élément)` dans le heap, où la priorité est utilisée pour ordonner les éléments.