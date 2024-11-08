# Outline : Suffix Arrays (Tableaux de Suffixes)

## Introduction aux Suffix Arrays

Un **Suffix Array** (ou tableau de suffixes) est une structure de données qui contient tous les suffixes triés d'une chaîne de caractères. Il est souvent utilisé dans des algorithmes de manipulation de chaînes de caractères pour accélérer les recherches et résoudre des problèmes de sous-chaînes.

### Qu'est-ce qu'un Suffix Array ?

Pour une chaîne donnée `S` de longueur `n`, un **Suffix Array** est un tableau des `n` suffixes de `S`, triés par ordre lexicographique. Chaque suffixe est représenté par son index de début dans la chaîne.

- **Exemple** : Pour la chaîne `banana`, les suffixes sont :
  - `banana`, `anana`, `nana`, `ana`, `na`, `a`
  - En les triant par ordre lexicographique, le Suffix Array contient leurs indices : `[5, 3, 1, 0, 4, 2]`

Le Suffix Array est utile car il permet d'accéder rapidement aux sous-chaînes de manière ordonnée et peut être utilisé pour des recherches de motifs (pattern matching) et d'autres problèmes liés aux sous-chaînes.

### Propriétés des Suffix Arrays

- **Accès rapide** aux suffixes triés.
- **Espace efficace** : Les Suffix Arrays nécessitent moins de mémoire que d'autres structures comme les arbres de suffixes.
- **Permet des recherches binaires** : Grâce à l'ordre lexicographique, on peut utiliser des recherches binaires pour trouver des motifs.

## Longest Common Prefix (LCP) Array

Le **LCP Array** est une structure complémentaire au Suffix Array. Il stocke la longueur du préfixe commun le plus long entre chaque paire de suffixes adjacents dans le Suffix Array.

### Qu'est-ce que le LCP Array ?

Pour une chaîne de caractères `S` et son Suffix Array, le **LCP Array** à l'index `i` contient la longueur du préfixe commun le plus long entre les suffixes aux positions `i` et `i+1` dans le Suffix Array.

- **Exemple** : Pour la chaîne `banana` et son Suffix Array `[5, 3, 1, 0, 4, 2]`, le LCP Array pourrait ressembler à `[1, 3, 0, 0, 2, 1]`.

Le LCP Array est utilisé pour des tâches de **comparaison rapide de sous-chaînes**, et pour résoudre des problèmes tels que la **longest common substring** (plus longue sous-chaîne commune) ou la **longest repeated substring** (plus longue sous-chaîne répétée).

## Applications des Suffix Arrays

Les Suffix Arrays sont utiles dans divers problèmes de traitement de chaînes de caractères :

### 1. **Recherche de Sous-chaînes**

- **Description** : Étant donné une chaîne `S` et un motif `P`, on veut vérifier si `P` est une sous-chaîne de `S`.
- **Utilisation du Suffix Array** : En effectuant une recherche binaire dans le Suffix Array, on peut trouver efficacement le motif dans la chaîne de base.

### 2. **Nombre de Sous-chaînes Uniques**

- **Description** : Compter toutes les sous-chaînes uniques d'une chaîne `S`.
- **Utilisation du Suffix Array et du LCP Array** : En utilisant la différence entre les longueurs des suffixes consécutifs dans le Suffix Array et les valeurs du LCP Array, on peut calculer le nombre de sous-chaînes uniques.

### 3. **Longest Common Substring (LCS)**

- **Description** : Trouver la plus longue sous-chaîne commune entre deux chaînes.
- **Utilisation du Suffix Array** : En combinant les Suffix Arrays des deux chaînes et en analysant le LCP Array résultant, on peut déterminer la plus longue sous-chaîne commune.

### 4. **Longest Repeated Substring**

- **Description** : Trouver la plus longue sous-chaîne qui se répète au moins une fois dans une chaîne donnée.
- **Utilisation du Suffix Array et du LCP Array** : La longueur maximale du LCP Array donne la longueur de la plus longue sous-chaîne répétée.

## Détails de l'Implémentation

### Construction d'un Suffix Array

La construction naïve d'un Suffix Array prend O(n^2 log n) car il faut trier `n` suffixes de longueur `n`. Cependant, des algorithmes optimisés comme **l'algorithme de saisies doubles** permettent de construire un Suffix Array en O(n log n).

### Queries (Recherches) sur les Suffix Arrays

Les recherches de motifs dans un Suffix Array peuvent être effectuées efficacement avec une recherche binaire, grâce à l'ordre lexicographique des suffixes.

### LCP Array Construction

Le LCP Array peut être construit en O(n) à partir du Suffix Array. Cela nécessite de comparer chaque paire de suffixes adjacents dans l'ordre donné par le Suffix Array.

## Exemple d'Implémentation en Python

Voici un exemple simple d'implémentation d'un Suffix Array avec un LCP Array en Python.

```python
def build_suffix_array(s):
    suffixes = [(s[i:], i) for i in range(len(s))]
    suffixes.sort()
    suffix_array = [suffix[1] for suffix in suffixes]
    return suffix_array

def build_lcp_array(s, suffix_array):
    n = len(s)
    rank = [0] * n
    lcp = [0] * n
    for i, suffix in enumerate(suffix_array):
        rank[suffix] = i
    h = 0
    for i in range(n):
        if rank[i] > 0:
            j = suffix_array[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1
    return lcp

# Exemple d'utilisation
s = "banana"
suffix_array = build_suffix_array(s)
lcp_array = build_lcp_array(s, suffix_array)
print("Suffix Array:", suffix_array)
print("LCP Array:", lcp_array)
```

##  Explication du Code :

- La fonction `build_suffix_array` construit un Suffix Array pour une chaîne `s` donnée.
- La fonction `build_lcp_array` construit un LCP Array à partir du Suffix Array et de la chaîne `s`.
- Les fonctions utilisent des comparaisons de suffixes pour construire le LCP Array.

Les Suffix Arrays et LCP Arrays sont des structures de données puissantes pour résoudre des problèmes de sous-chaînes et de manipulation de chaînes de caractères de manière efficace.

## Conclusion :
Les Suffix Arrays sont une structure de données puissante pour résoudre des problèmes complexes de manipulation de chaînes de caractères. En les combinant avec le LCP Array, ils permettent d'effectuer des recherches rapides et d'optimiser des calculs sur des sous-chaînes. Bien que la construction des Suffix Arrays puisse être complexe, ils sont essentiels pour les algorithmes d'optimisation de texte et sont couramment utilisés dans des applications de traitement de texte et de bioinformatique.