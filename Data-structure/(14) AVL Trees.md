# Outline : AVL Trees (Arbres AVL)

## Introduction aux AVL Trees

Un **AVL Tree** (Arbre AVL) est un type particulier d'arbre binaire de recherche (BST) qui maintient un équilibre pour garantir une recherche, insertion et suppression efficaces. Dans un AVL Tree, la différence de hauteur entre les sous-arbres gauche et droit de chaque nœud ne dépasse jamais 1. Cela garantit que l'arbre reste **équilibré**, offrant des performances optimales.

### Pourquoi Utiliser un AVL Tree ?

Les AVL Trees sont utiles pour éviter que l'arbre ne devienne trop déséquilibré, ce qui peut ralentir les opérations. Dans un BST classique, si l'arbre devient trop déséquilibré (par exemple, s'il devient une "liste" dans le pire des cas), les performances des opérations passent de O(log n) à O(n). L'AVL Tree résout ce problème en effectuant des **rotations** pour rééquilibrer l'arbre dès qu'un déséquilibre est détecté.

### Propriétés des AVL Trees

- **Équilibrage automatique** : Maintient une hauteur équilibrée après chaque insertion ou suppression.
- **Complexité garantie** : Les opérations de recherche, insertion et suppression se font en O(log n).
- **Rotations** : Utilise des rotations pour rétablir l'équilibre, telles que la rotation gauche, droite, double rotation gauche-droite, et double rotation droite-gauche.

## Types de Rotations

Les **rotations** sont des opérations qui réorganisent les nœuds pour maintenir l'équilibre de l'arbre.

### 1. Rotation Droite (Right Rotation)

- Utilisée lorsque le sous-arbre gauche d'un nœud est plus lourd que le sous-arbre droit.
- Permet de rééquilibrer l'arbre en déplaçant le nœud du sous-arbre gauche vers le haut.

### 2. Rotation Gauche (Left Rotation)

- Utilisée lorsque le sous-arbre droit d'un nœud est plus lourd que le sous-arbre gauche.
- Permet de rééquilibrer l'arbre en déplaçant le nœud du sous-arbre droit vers le haut.

### 3. Double Rotation Gauche-Droite (Left-Right Rotation)

- Utilisée lorsque le déséquilibre se situe dans le sous-arbre gauche du sous-arbre droit d'un nœud.
- Consiste en une rotation gauche suivie d'une rotation droite.

### 4. Double Rotation Droite-Gauche (Right-Left Rotation)

- Utilisée lorsque le déséquilibre se situe dans le sous-arbre droit du sous-arbre gauche d'un nœud.
- Consiste en une rotation droite suivie d'une rotation gauche.

## Opérations sur un AVL Tree

### Insertion

Lorsqu'un nouvel élément est inséré dans un AVL Tree, il est d'abord ajouté comme dans un arbre binaire de recherche classique. Ensuite, on vérifie l'équilibre de l'arbre et, si nécessaire, on effectue des rotations pour rétablir l'équilibre.

### Suppression

La suppression d'un élément suit le même principe : l'élément est d'abord supprimé comme dans un BST, puis des rotations sont effectuées si le déséquilibre dépasse 1.

### Maintien de l'Équilibre

À chaque insertion ou suppression, on calcule le "facteur d'équilibre" (balance factor) pour chaque nœud. Ce facteur indique si un nœud est équilibré (0), légèrement déséquilibré (-1 ou +1), ou fortement déséquilibré (≤ -2 ou ≥ +2). Les rotations sont appliquées en fonction de ce facteur.

## Exemple de Code en Python pour un AVL Tree

Voici une implémentation simple d'un AVL Tree en Python avec les opérations d'insertion, suppression et rééquilibrage.

```python
class Node:
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droite = None
        self.hauteur = 1

class AVLTree:
    def get_height(self, noeud):
        if not noeud:
            return 0
        return noeud.hauteur

    def get_balance(self, noeud):
        if not noeud:
            return 0
        return self.get_height(noeud.gauche) - self.get_height(noeud.droite)

    def rotate_right(self, y):
        x = y.gauche
        T2 = x.droite
        x.droite = y
        y.gauche = T2
        y.hauteur = 1 + max(self.get_height(y.gauche), self.get_height(y.droite))
        x.hauteur = 1 + max(self.get_height(x.gauche), self.get_height(x.droite))
        return x

    def rotate_left(self, x):
        y = x.droite
        T2 = y.gauche
        y.gauche = x
        x.droite = T2
        x.hauteur = 1 + max(self.get_height(x.gauche), self.get_height(x.droite))
        y.hauteur = 1 + max(self.get_height(y.gauche), self.get_height(y.droite))
        return y

    def insert(self, noeud, valeur):
        if not noeud:
            return Node(valeur)
        elif valeur < noeud.valeur:
            noeud.gauche = self.insert(noeud.gauche, valeur)
        else:
            noeud.droite = self.insert(noeud.droite, valeur)

        noeud.hauteur = 1 + max(self.get_height(noeud.gauche), self.get_height(noeud.droite))
        balance = self.get_balance(noeud)

        # Rotation Droite
        if balance > 1 and valeur < noeud.gauche.valeur:
            return self.rotate_right(noeud)

        # Rotation Gauche
        if balance < -1 and valeur > noeud.droite.valeur:
            return self.rotate_left(noeud)

        # Rotation Gauche-Droite
        if balance > 1 and valeur > noeud.gauche.valeur:
            noeud.gauche = self.rotate_left(noeud.gauche)
            return self.rotate_right(noeud)

        # Rotation Droite-Gauche
        if balance < -1 and valeur < noeud.droite.valeur:
            noeud.droite = self.rotate_right(noeud.droite)
            return self.rotate_left(noeud)

        return noeud

# Exemple d'utilisation
avl_tree = AVLTree()
racine = None
valeurs = [10, 20, 30, 40, 50, 25]
for valeur in valeurs:
    racine = avl_tree.insert(racine, valeur)
```

## 