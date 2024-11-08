# Introduction aux Linked Lists (Listes Chaînées)

Les **Linked Lists** ou **listes chaînées** sont une structure de données fondamentale utilisée pour stocker une séquence d'éléments. Contrairement aux tableaux, où les éléments sont stockés en mémoire de manière contiguë, les listes chaînées stockent chaque élément (appelé **nœud**) avec un lien vers l'élément suivant, formant une chaîne d'éléments.

## Structure de Base d'une Linked List

Chaque **nœud** dans une liste chaînée contient deux parties :

1. **Valeur** : La donnée que le nœud représente.
2. **Lien** (ou **référence/pointeur**) : Une référence vers le nœud suivant dans la séquence.

La liste commence avec un **nœud de tête** (head node) et se termine avec un **nœud de queue** qui ne pointe vers aucun autre nœud (généralement défini comme `None`).

### Types de Linked Lists

1. **Liste Chaînée Simple** (Singly Linked List) : Chaque nœud pointe uniquement vers le nœud suivant.
2. **Liste Doublement Chaînée** (Doubly Linked List) : Chaque nœud a un lien vers le nœud suivant et le nœud précédent, permettant de naviguer dans les deux sens.
3. **Liste Circulaire** (Circular Linked List) : Le dernier nœud pointe vers le premier nœud, formant un cycle.

## Avantages des Linked Lists

- **Insertion et Suppression Rapides** : Ajouter ou supprimer un élément est rapide, surtout si l'on connaît déjà l'emplacement du nœud. Contrairement aux tableaux, les listes chaînées n'ont pas besoin de déplacer les éléments.
- **Taille Dynamique** : Contrairement aux tableaux statiques, une liste chaînée peut facilement grandir ou rétrécir, car elle n'a pas de taille fixe.
- **Allocation de Mémoire Flexible** : Chaque nœud est stocké indépendamment en mémoire, ce qui permet une utilisation plus efficace dans certaines situations.

## Inconvénients des Linked Lists

- **Accès Lent aux Éléments** : Contrairement aux tableaux, il n'est pas possible d'accéder directement à un élément par son index. Pour accéder à un élément spécifique, il faut parcourir la liste depuis le début (complexité O(n)).
- **Utilisation de Mémoire Supplémentaire** : Chaque nœud nécessite un espace mémoire supplémentaire pour stocker la référence vers le nœud suivant (et parfois le nœud précédent).

## Cas d'Utilisation des Linked Lists

Les Linked Lists sont utiles dans des situations où :

- **Les insertions et suppressions fréquentes** sont nécessaires, surtout au début ou à la fin de la liste.
- **La taille des données varie beaucoup** et n'est pas connue à l'avance, rendant les tableaux dynamiques inefficaces ou coûteux en mémoire.
- **Les structures de données flexibles** comme les files d'attente et les piles doivent être implémentées. Les listes chaînées peuvent facilement représenter une file d'attente (FIFO) ou une pile (LIFO).

## Exemples d'Implémentation en Python

### 1. Liste Chaînée Simple (Singly Linked List)

Dans une liste chaînée simple, chaque nœud pointe uniquement vers le nœud suivant.

```python
class Node:
    def __init__(self, valeur):
        self.valeur = valeur
        self.suivant = None

class SinglyLinkedList:
    def __init__(self):
        self.tete = None

    def append(self, valeur):
        nouveau_noeud = Node(valeur)
        if not self.tete:
            self.tete = nouveau_noeud
            return
        dernier = self.tete
        while dernier.suivant:
            dernier = dernier.suivant
        dernier.suivant = nouveau_noeud

    def afficher(self):
        noeud_actuel = self.tete
        while noeud_actuel:
            print(noeud_actuel.valeur, end=" -> ")
            noeud_actuel = noeud_actuel.suivant
        print("None")

# Utilisation de la liste chaînée simple
ma_liste = SinglyLinkedList()
ma_liste.append(10)
ma_liste.append(20)
ma_liste.append(30)
ma_liste.afficher()  # Sortie : 10 -> 20 -> 30 -> None
```

### 2. Liste Doublement Chaînée (Doubly Linked List)

Dans une liste doublement chaînée, chaque nœud a des références au nœud suivant et au nœud précédent, permettant une navigation dans les deux sens.

```python

class DoubleNode:
    def __init__(self, valeur):
        self.valeur = valeur
        self.suivant = None
        self.precedent = None

class DoublyLinkedList:
    def __init__(self):
        self.tete = None

    def append(self, valeur):
        nouveau_noeud = DoubleNode(valeur)
        if not self.tete:
            self.tete = nouveau_noeud
            return
        dernier = self.tete
        while dernier.suivant:
            dernier = dernier.suivant
        dernier.suivant = nouveau_noeud
        nouveau_noeud.precedent = dernier

    def afficher(self):
        noeud_actuel = self.tete
        while noeud_actuel:
            print(noeud_actuel.valeur, end=" <-> ")
            noeud_actuel = noeud_actuel.suivant
        print("None")

# Utilisation de la liste doublement chaînée
ma_liste_double = DoublyLinkedList()
ma_liste_double.append(10)
ma_liste_double.append(20)
ma_liste_double.append(30)
ma_liste_double.afficher()  # Sortie : 10 <-> 20 <-> 30 <-> None

``` 

### 3. Liste Circulaire (Circular Linked List)

Dans une liste circulaire, le dernier nœud pointe vers le premier nœud, formant un cycle.

```python

class CircularNode:
    def __init__(self, valeur):
        self.valeur = valeur
        self.suivant = None

class CircularLinkedList:
    def __init__(self):
        self.tete = None

    def append(self, valeur):
        nouveau_noeud = CircularNode(valeur)
        if not self.tete:
            self.tete = nouveau_noeud
            nouveau_noeud.suivant = self.tete
            return
        dernier = self.tete
        while dernier.suivant != self.tete:
            dernier = dernier.suivant
        dernier.suivant = nouveau_noeud
        nouveau_noeud.suivant = self.tete

    def afficher(self):
        noeud_actuel = self.tete
        if not self.tete:
            return
        while True:
            print(noeud_actuel.valeur, end=" -> ")
            noeud_actuel = noeud_actuel.suivant
            if noeud_actuel == self.tete:
                break
        print("(retour au début)")

# Utilisation de la liste circulaire
ma_liste_circulaire = CircularLinkedList()
ma_liste_circulaire.append(10)
ma_liste_circulaire.append(20)
ma_liste_circulaire.append(30)
ma_liste_circulaire.afficher()  # Sortie : 10 -> 20 -> 30 -> (retour au début)

```

## Conclusion

Les Linked Lists sont une structure de données flexible et efficace dans certains cas, mais elles ne conviennent pas à toutes les situations. Chaque type de Linked List a ses propres applications :

- Liste Chaînée Simple : Idéale pour une séquence de données simple avec insertion à la fin.
- Liste Doublement Chaînée : Pratique pour des opérations nécessitant une navigation dans les deux sens, comme dans un historique de navigation.
- Liste Circulaire : Utile pour des structures de données circulaires, comme une playlist de musique en boucle.
Lorsqu'une application nécessite des insertions et des suppressions fréquentes ou que la taille des données varie de manière dynamique, les Linked Lists sont un excellent choix. Cependant, pour un accès direct et rapide aux éléments, un tableau est généralement plus adapté.