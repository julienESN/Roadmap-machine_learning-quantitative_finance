# Hash Table et Fonction de Hachage

## Qu'est-ce qu'une Table de Hachage (Hash Table) et une Fonction de Hachage ?

Une **table de hachage** est une structure de données qui permet de stocker et de récupérer des paires clé-valeur de manière efficace. Elle utilise une **fonction de hachage** pour convertir une clé en un index dans un tableau, facilitant un accès quasi constant aux données.

- **Fonction de hachage** : Une fonction qui prend une clé en entrée et renvoie un index unique. Elle permet d'accéder rapidement aux valeurs associées dans la table.
- **But** : Optimiser l'accès aux données pour des opérations comme l'insertion, la recherche et la suppression.

Les tables de hachage sont largement utilisées dans des applications où des recherches rapides sont nécessaires, comme les bases de données, les caches, et les tables de routage.

## Propriétés des Fonctions de Hachage

Une fonction de hachage efficace doit respecter les propriétés suivantes :

1. **Uniformité** : Les clés doivent être réparties de manière uniforme dans la table de hachage pour minimiser les collisions.
2. **Déterminisme** : La même clé doit toujours produire le même index.
3. **Performance** : Le calcul de la fonction de hachage doit être rapide pour garantir une insertion et une recherche efficaces.

## Gestion des Collisions

Lorsque deux clés différentes produisent le même index, une **collision** se produit. Il existe deux méthodes principales pour résoudre les collisions :

- **Separate Chaining (chaînage séparé)** : Chaque emplacement dans la table pointe vers une liste qui stocke toutes les paires clé-valeur ayant le même index.
- **Open Addressing (adressage ouvert)** : Plutôt que de créer une liste, on cherche une autre case libre dans la table pour insérer la nouvelle paire.

### Separate Chaining

Dans cette méthode, chaque emplacement de la table contient une liste (ou chaîne) de toutes les valeurs ayant le même index. Quand une collision se produit, la nouvelle valeur est ajoutée à cette liste.

#### Avantages :

- Simple à mettre en œuvre.
- Pas de limite sur le nombre d'éléments que l'on peut ajouter, tant que la mémoire le permet.

#### Inconvénients :

- Peut utiliser beaucoup de mémoire en cas de nombreuses collisions.
- La complexité de recherche et d'insertion peut augmenter si de nombreuses collisions se produisent.

### Open Addressing

Dans l'adressage ouvert, lorsqu'une collision se produit, on trouve une nouvelle case dans la table pour y insérer la valeur. Il existe plusieurs techniques d'open addressing :

1. **Linear Probing** : On vérifie les cases suivantes de manière linéaire jusqu'à trouver une case libre.
2. **Quadratic Probing** : On saute de plus en plus loin en utilisant une fonction quadratique pour réduire l'agrégation des clés.
3. **Double Hashing** : On utilise une seconde fonction de hachage pour déterminer la distance à parcourir jusqu'à la prochaine case libre.

#### Avantages :

- Utilise moins de mémoire que le chaînage séparé.
- Peut être plus rapide en l'absence de trop nombreuses collisions.

#### Inconvénients :

- Si la table est presque pleine, les collisions peuvent entraîner des performances dégradées.
- Une table de hachage avec open addressing nécessite un taux de remplissage faible pour maintenir des performances optimales.

## Analyse de Complexité

Pour une table de hachage bien équilibrée (faible nombre de collisions) :

| Opération   | Complexité Moyenne | Complexité Pire Cas |
| ----------- | ------------------ | ------------------- |
| Insertion   | O(1)               | O(n)                |
| Recherche   | O(1)               | O(n)                |
| Suppression | O(1)               | O(n)                |

En cas de collisions fréquentes, la complexité peut se dégrader, notamment pour les méthodes d'open addressing si le tableau est presque plein.

## Détails de l'Implémentation du Chaînage Séparé

Dans l'approche de chaînage séparé, chaque case de la table contient une liste chaînée pour stocker les paires clé-valeur. Lorsqu'une collision se produit, la nouvelle paire est ajoutée à la liste de l'emplacement de la collision.

### Vue d'ensemble de l'Approche avec Liste Chaînée

Chaque emplacement de la table est soit vide, soit contient une liste chaînée. En cas de collision, les paires clé-valeur sont ajoutées à cette liste.

#### Questions Fréquemment Posées sur le Chaînage Séparé

- **Que se passe-t-il si toutes les clés se hachent au même index ?**  
  La complexité de recherche, insertion et suppression dans la liste chaînée devient O(n).
- **Comment éviter les listes longues ?**  
  Une fonction de hachage bien conçue et une taille de table appropriée peuvent minimiser le nombre de collisions.

### Exemple de Code de Chaînage Séparé

```python
class HashTableSeparateChaining:
    def __init__(self, taille=10):
        self.table = [[] for _ in range(taille)]

    def _hash_function(self, cle):
        return hash(cle) % len(self.table)

    def inserer(self, cle, valeur):
        index = self._hash_function(cle)
        for i, (k, v) in enumerate(self.table[index]):
            if k == cle:
                self.table[index][i] = (cle, valeur)
                return
        self.table[index].append((cle, valeur))

    def rechercher(self, cle):
        index = self._hash_function(cle)
        for k, v in self.table[index]:
            if k == cle:
                return v
        return None

    def supprimer(self, cle):
        index = self._hash_function(cle)
        for i, (k, v) in enumerate(self.table[index]):
            if k == cle:
                del self.table[index][i]
                return True
        return False
```

## Open Addressing : Détails et Implémentation

Linear Probing (Sondage Linéaire)
Dans le sondage linéaire, en cas de collision, on vérifie les cases suivantes de manière séquentielle.

```python

class HashTableLinearProbing:
    def __init__(self, taille=10):
        self.table = [None] * taille

    def _hash_function(self, cle):
        return hash(cle) % len(self.table)

    def inserer(self, cle, valeur):
        index = self._hash_function(cle)
        while self.table[index] is not None:
            if self.table[index][0] == cle:
                self.table[index] = (cle, valeur)
                return
            index = (index + 1) % len(self.table)
        self.table[index] = (cle, valeur)

    def rechercher(self, cle):
        index = self._hash_function(cle)
        while self.table[index] is not None:
            if self.table[index][0] == cle:
                return self.table[index][1]
            index = (index + 1) % len(self.table)
        return None

    def supprimer(self, cle):
        index = self._hash_function(cle)
        while self.table[index] is not None:
            if self.table[index][0] == cle:
                self.table[index] = None
                return True
            index = (index + 1) % len(self.table)
        return False
``` 

# Quadratic Probing (Sondage Quadratique)
Le sondage quadratique utilise une fonction quadratique pour déterminer la prochaine case en cas de collision, réduisant ainsi les clusters de clés.

# Double Hashing
Dans le double hachage, une seconde fonction de hachage est utilisée pour déterminer le déplacement en cas de collision, offrant une solution efficace pour répartir les clés.

## Conclusion

Les tables de hachage sont une structure de données puissante pour la recherche rapide. Les techniques de résolution des collisions, comme le chaînage séparé et l'adressage ouvert, permettent de gérer efficacement les cas où plusieurs clés produisent le même index.

- Chaînage Séparé : Utilise une liste chaînée pour chaque emplacement de la table. Simple à mettre en œuvre, mais peut être inefficace si les listes deviennent trop longues.

- Adressage Ouvert : Évite les listes en trouvant un nouvel emplacement pour chaque collision, avec plusieurs techniques comme le sondage linéaire, quadratique et le double hachage.