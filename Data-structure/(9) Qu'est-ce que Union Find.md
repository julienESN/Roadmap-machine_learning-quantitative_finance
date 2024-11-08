# Outline

## Discussion et Exemples

### Qu'est-ce que Union Find ?
Le **Union Find** (ou **Disjoint Set Union - DSU**) est une structure de données utilisée pour suivre et gérer la partition d'un ensemble d'éléments en sous-ensembles disjoints. Il permet deux opérations principales :
- **Find** : Trouver le représentant ou le "parent" d'un élément, indiquant à quel sous-ensemble il appartient.
- **Union** : Fusionner deux sous-ensembles en un seul.

Cette structure est particulièrement utile pour des applications où l'on a besoin de vérifier si deux éléments font partie du même sous-ensemble ou pour construire des regroupements dynamiques.

### Exemple avec des Aimants
Imaginons des aimants qui se connectent pour former des groupes distincts. Chaque groupe d'aimants représente un sous-ensemble, et les aimants connectés forment un ensemble de sous-ensembles disjoints. En utilisant Union Find, on peut gérer les regroupements d'aimants et déterminer si deux aimants sont connectés dans le même sous-ensemble.

### Quand et Où Utiliser Union Find ?
Union Find est utilisé dans divers domaines en informatique, notamment :
- **Algorithmes de graphes** : Comme dans l'algorithme de Kruskal pour construire un arbre couvrant de poids minimal (Minimum Spanning Tree - MST).
- **Systèmes de réseaux sociaux** : Pour vérifier si deux personnes sont dans le même réseau ou groupe.
- **Gestion de groupes dynamiques** : Comme les regroupements de zones ou de clusters dans des jeux ou des simulations.

### Algorithme de l'Arbre Couvant Minimum de Kruskal
L'algorithme de Kruskal est utilisé pour trouver un arbre couvrant de poids minimal dans un graphe pondéré. Union Find joue un rôle essentiel dans cet algorithme pour éviter les cycles lors de l'ajout d'arêtes :
1. On trie toutes les arêtes par poids.
2. On ajoute chaque arête au MST, à condition qu'elle ne forme pas de cycle avec les arêtes déjà ajoutées. Cela est vérifié en utilisant Union Find pour s'assurer que les deux nœuds de l'arête appartiennent à des sous-ensembles disjoints.

### Analyse de Complexité
L'implémentation naïve de Union Find est relativement inefficace, mais avec des optimisations comme **compression de chemin** (path compression) et **union by rank** (union par rang), la complexité est presque constante, notée **O(α(n))**, où **α(n)** est l'inverse de la fonction d'Ackermann, une fonction qui croît extrêmement lentement.

## Détails de l'Implémentation

### Opérations Find et Union

- **Find** : Permet de retrouver le représentant ou le parent d'un élément, déterminant le sous-ensemble auquel il appartient. Avec l'optimisation de compression de chemin, l'opération rend le parcours plus efficace en rattachant directement les éléments à leur représentant lors de la recherche.
  
- **Union** : Permet de fusionner deux sous-ensembles. En utilisant l'optimisation de "union par rang", on rattache toujours l'arbre de plus petite hauteur sous l'arbre de plus grande hauteur, ce qui minimise la profondeur de l'arbre.

### Compression de Chemin (Path Compression)
La **compression de chemin** est une optimisation appliquée lors de l'opération Find. Elle permet de raccourcir les chemins dans l'arbre en rattachant directement les éléments à leur représentant final. Cela améliore l'efficacité de l'opération Find pour les futurs appels.

## Implémentation en Code

Voici une implémentation simple de la structure Union Find avec compression de chemin et union par rang en Python :

```python
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size  # Initialisation du rang de chaque nœud à 1

    # Find avec compression de chemin
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])  # Compression de chemin
        return self.root[x]

    # Union avec union par rang
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    # Vérification si deux éléments sont connectés
    def connected(self, x, y):
        return self.find(x) == self.find(y)

# Exemple d'utilisation de Union Find
uf = UnionFind(10)
uf.union(1, 2)
uf.union(2, 3)
print(uf.connected(1, 3))  # Sortie : True
print(uf.connected(1, 4))  # Sortie : False

```

## Explication du Code

- find(x) : Cette méthode utilise la compression de chemin pour retrouver le représentant de l'élément x.
- union(x, y) : Cette méthode fusionne les sous-ensembles contenant les éléments x et y en utilisant l'union par rang pour minimiser la hauteur de l'arbre.
- connected(x, y) : Cette méthode vérifie si les éléments x et y sont connectés dans le même sous-ensemble.
