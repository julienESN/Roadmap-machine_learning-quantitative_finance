# Outline

## Discussion et Exemples

### Qu'est-ce qu'un Arbre Binaire (Binary Tree - BT) ?

Un **arbre binaire** est une structure de données arborescente où chaque nœud a au maximum deux enfants, appelés **enfant gauche** et **enfant droit**. Cette structure est utile pour organiser les données de manière hiérarchique, permettant un accès, une insertion et une suppression relativement efficaces.

Les arbres binaires peuvent être de différents types :

- **Arbre binaire complet** : Tous les niveaux sont complètement remplis, sauf peut-être le dernier niveau, qui est rempli de gauche à droite.
- **Arbre binaire parfait** : Tous les niveaux sont complètement remplis.
- **Arbre binaire dégénéré** : Chaque nœud a exactement un enfant, ce qui le rend similaire à une liste chaînée.

### Qu'est-ce qu'un Arbre Binaire de Recherche (Binary Search Tree - BST) ?

Un **arbre binaire de recherche** (BST) est un type particulier d'arbre binaire où chaque nœud suit une **propriété de recherche** spécifique :

- Le sous-arbre gauche d'un nœud contient uniquement des nœuds avec des valeurs inférieures à la valeur de ce nœud.
- Le sous-arbre droit d'un nœud contient uniquement des nœuds avec des valeurs supérieures à la valeur de ce nœud.

Cette propriété permet de rechercher efficacement des valeurs dans un BST, car on peut rapidement éliminer la moitié des nœuds à chaque comparaison, en fonction de la valeur recherchée.

### Où Utiliser les Arbres Binaires et les Arbres Binaires de Recherche ?

Les BT et BST sont utilisés dans de nombreux domaines en informatique, notamment :

- **Structures de données et algorithmes de tri** : Les BST sont souvent utilisés pour implémenter des structures comme les tables de symboles et les dictionnaires, où l'efficacité de la recherche est cruciale.
- **Applications de recherche** : Les BST sont adaptés pour les applications qui nécessitent des recherches rapides et ordonnées, comme les bases de données et les systèmes de fichiers.
- **Expressions arithmétiques** : Les arbres binaires sont souvent utilisés pour représenter des expressions arithmétiques, chaque nœud contenant un opérateur ou une valeur.
- **Parcours de graphes** : Les arbres binaires sont utilisés dans des algorithmes comme DFS (Depth-First Search) et BFS (Breadth-First Search) pour le parcours de graphes.

### Analyse de Complexité

Pour les opérations de base sur un BST équilibré (où la profondeur des sous-arbres est approximativement égale) :

| Opération   | Complexité (Cas Équilibré) | Complexité (Cas Dégradé) |
| ----------- | -------------------------- | ------------------------ |
| Recherche   | O(log n)                   | O(n)                     |
| Insertion   | O(log n)                   | O(n)                     |
| Suppression | O(log n)                   | O(n)                     |

Dans le **meilleur cas** (arbre équilibré), la complexité est logarithmique car à chaque étape, on divise le nombre de nœuds à traiter par deux. Cependant, dans le **pire cas** (arbre dégénéré ressemblant à une liste chaînée), la complexité devient linéaire car on doit parcourir tous les nœuds pour trouver une valeur.

## Implémentation en Code

Voici un exemple d'implémentation d'un **Binary Search Tree (BST)** en Python :

```python
class Node:
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droit = None

class BST:
    def __init__(self):
        self.racine = None

    # Insertion d'une valeur dans le BST
    def inserer(self, valeur):
        if self.racine is None:
            self.racine = Node(valeur)
        else:
            self._inserer_recursif(self.racine, valeur)

    def _inserer_recursif(self, noeud, valeur):
        if valeur < noeud.valeur:
            if noeud.gauche is None:
                noeud.gauche = Node(valeur)
            else:
                self._inserer_recursif(noeud.gauche, valeur)
        else:
            if noeud.droit is None:
                noeud.droit = Node(valeur)
            else:
                self._inserer_recursif(noeud.droit, valeur)

    # Recherche d'une valeur dans le BST
    def rechercher(self, valeur):
        return self._rechercher_recursif(self.racine, valeur)

    def _rechercher_recursif(self, noeud, valeur):
        if noeud is None or noeud.valeur == valeur:
            return noeud is not None
        if valeur < noeud.valeur:
            return self._rechercher_recursif(noeud.gauche, valeur)
        else:
            return self._rechercher_recursif(noeud.droit, valeur)

    # Affichage en ordre croissant (parcours en ordre)
    def parcours_en_ordre(self):
        self._parcours_en_ordre_recursif(self.racine)

    def _parcours_en_ordre_recursif(self, noeud):
        if noeud is not None:
            self._parcours_en_ordre_recursif(noeud.gauche)
            print(noeud.valeur, end=" ")
            self._parcours_en_ordre_recursif(noeud.droit)

# Utilisation du BST
bst = BST()
bst.inserer(10)
bst.inserer(5)
bst.inserer(15)
bst.inserer(7)

print("Recherche 7 dans le BST :", bst.rechercher(7))  # Sortie : True
print("Recherche 3 dans le BST :", bst.rechercher(3))  # Sortie : False

print("Parcours en ordre croissant : ", end="")
bst.parcours_en_ordre()  # Sortie : 5 7 10 15

```

## Explication du Code :

- insert : Insère une valeur dans le BST en suivant la propriété de recherche.
- search : Recherche une valeur dans le BST en suivant la propriété de recherche.
- inorder traversal : Parcourt le BST en ordre croissant (gauche-racine-droit).

Avec ces concepts et cette implémentation, tu devrais maintenant mieux comprendre comment fonctionnent les arbres binaires et les arbres binaires de recherche, ainsi que leurs cas d'utilisation et leur efficacité.

