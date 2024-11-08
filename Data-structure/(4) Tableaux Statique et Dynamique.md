# Tableaux Statique et Dynamique

En programmation, les tableaux (arrays) sont utilisés pour stocker des collections d'éléments. Il existe deux types principaux de tableaux : les **tableaux statiques** et les **tableaux dynamiques**.

## Tableau Statique

Un **tableau statique** est un tableau de taille fixe, ce qui signifie que la taille du tableau est déterminée au moment de sa création et ne peut pas être modifiée. Ce type de tableau est plus efficace en termes de mémoire, car il ne nécessite pas de réallocation ou de redimensionnement pendant l'exécution. Cependant, il manque de flexibilité pour des applications où la taille des données peut changer.

### Exemple de Tableau Statique en Python

En Python, les tableaux statiques ne sont pas directement pris en charge comme dans certains langages (comme C). Cependant, on peut utiliser des listes avec une taille fixe ou le module `array` pour simuler un tableau statique.

```python
# Utilisation d'une liste de taille fixe pour simuler un tableau statique
taille = 5
tableau_statique = [0] * taille  # Initialisé avec des zéros

# Accès et modification d'un élément
tableau_statique[2] = 10
print("Tableau statique :", tableau_statique)
```

## Limitation des Tableaux Statiques

- **Taille Fixe** : La taille du tableau doit être définie à l'avance et ne peut pas être modifiée.
- **Utilisation de la mémoire** : Adapté lorsque la taille des données est connue à l'avance.

## Tableau Dynamique

Un **tableau dynamique** est un tableau dont la taille peut changer. En Python, les listes fonctionnent comme des tableaux dynamiques. Cela signifie que nous pouvons ajouter, insérer ou supprimer des éléments à volonté. Les tableaux dynamiques sont très flexibles, mais leur redimensionnement peut consommer plus de mémoire et entraîner des ralentissements si le tableau est redimensionné fréquemment.

### Exemple de Tableau Dynamique en Python

En Python, les listes sont des tableaux dynamiques par défaut. Voici un exemple d'utilisation :

```python
# Création d'un tableau dynamique (liste)
tableau_dynamique = []

# Ajout d'éléments
tableau_dynamique.append(1)
tableau_dynamique.append(2)
tableau_dynamique.append(3)
print("Tableau dynamique après ajout :", tableau_dynamique)

# Insertion d'un élément à une position spécifique
tableau_dynamique.insert(1, 10)
print("Tableau dynamique après insertion :", tableau_dynamique)

# Suppression d'un élément
tableau_dynamique.pop(1)
print("Tableau dynamique après suppression :", tableau_dynamique)
```

## Avantages et Inconvénients du Tableau Dynamique

- **Flexibilité** :  Les tableaux dynamiques peuvent grandir ou rétrécir selon les besoins.
- **Complexité** : En raison des opérations de redimensionnement, les tableaux dynamiques peuvent être moins efficaces en mémoire et en temps d'exécution si des modifications fréquentes de taille sont nécessaires.

## Comparaison des Complexités

| Opération      | Tableau Statique | Tableau Dynamique |
|----------------|------------------|-------------------|
| Accès          | O(1)             | O(1)             |
| Recherche      | O(n)             | O(n)             |
| Insertion      | N/A              | O(n)             |
| Appending      | N/A              | O(1) amorti      |
| Suppression    | N/A              | O(n)             |

## Conclusion

- Tableaux statiques : Efficaces pour des données de taille fixe, mais manquent de flexibilité.
- Tableaux dynamiques : Flexibles et faciles à utiliser en Python grâce aux listes, mais peuvent être moins performants avec des modifications de taille fréquentes.
