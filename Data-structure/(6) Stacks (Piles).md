# Outline

## Discussion about Stacks

### What is a Stack?
Une **stack** (pile) est une structure de données qui suit le principe **LIFO** (Last In, First Out). Cela signifie que le dernier élément ajouté dans la pile sera le premier à être retiré. Imagine une pile d'assiettes : tu places une nouvelle assiette en haut, et tu retires toujours la dernière assiette ajoutée.

Les stacks ont deux opérations principales :
- **Push** : Ajouter un élément en haut de la pile.
- **Pop** : Retirer l'élément en haut de la pile.

### When and Where is a Stack Used?
Les stacks sont utilisées dans divers scénarios en programmation et dans le fonctionnement interne des systèmes. Voici quelques exemples :

- **Gestion des appels de fonctions** : Lorsque des fonctions s'appellent les unes les autres, le système utilise une stack pour garder une trace de l'ordre des appels.
- **Annuler (Undo)** dans les éditeurs de texte : Chaque action est empilée et peut être retirée pour annuler l'opération.
- **Parcours de structures de données** : Utilisé dans des algorithmes comme le parcours en profondeur (DFS) dans les graphes.
- **Vérification de syntaxe** : Utilisé pour vérifier les parenthèses équilibrées dans des expressions mathématiques ou dans le code.

### Complexity Analysis
Les opérations sur les stacks sont très efficaces car elles sont toutes réalisées sur le dernier élément de la pile (le haut de la pile) :

| Opération  | Complexité |
|------------|------------|
| Push       | O(1)       |
| Pop        | O(1)       |
| Peek       | O(1)       |

Les opérations **Push**, **Pop**, et **Peek** sont toutes réalisées en temps constant, ce qui rend les stacks très rapides pour la gestion de données selon le principe LIFO.

### Stack Usage Examples

1. **Navigation dans l'historique d'un navigateur** : Quand tu navigues sur un site, chaque page est ajoutée à la pile d'historique. Lorsque tu appuies sur le bouton "retour", la dernière page visitée est retirée de la pile.
2. **Annuler des actions** : Dans des logiciels comme Word ou Photoshop, les stacks sont utilisées pour empiler les actions. En appuyant sur "Ctrl + Z", on retire la dernière action de la pile.
3. **Évaluation d'expressions mathématiques** : Les stacks sont utilisées pour évaluer des expressions arithmétiques ou logiques, particulièrement pour transformer des notations infixes en postfixes (notation polonaise inversée).

## Implementation Details

### Pushing Elements on Stack
L'opération **Push** ajoute un élément en haut de la pile. Si la pile est implémentée avec une liste en Python, cela peut être fait avec la méthode `append`.

### Popping Elements from Stack
L'opération **Pop** retire l'élément du haut de la pile. Avec une liste Python, cela peut être fait avec la méthode `pop`.

## Code Implementation

Voici un exemple simple d'implémentation d'une stack en Python :

```python
class Stack:
    def __init__(self):
        self.items = []

    # Pushing an element onto the stack
    def push(self, item):
        self.items.append(item)
        print(f"Element {item} pushed onto stack")

    # Popping an element from the stack
    def pop(self):
        if not self.is_empty():
            popped_item = self.items.pop()
            print(f"Element {popped_item} popped from stack")
            return popped_item
        else:
            print("Stack is empty")
            return None

    # Checking the top element without removing it
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")
            return None

    # Checking if the stack is empty
    def is_empty(self):
        return len(self.items) == 0

    # Display the stack
    def display(self):
        print("Current Stack:", self.items)

# Utilisation de la stack
ma_stack = Stack()
ma_stack.push(10)
ma_stack.push(20)
ma_stack.push(30)
ma_stack.display()         # Affiche : Current Stack: [10, 20, 30]
print("Top element:", ma_stack.peek())  # Affiche le dernier élément : 30
ma_stack.pop()             # Retire 30 de la pile
ma_stack.display()         # Affiche : Current Stack: [10, 20]

```

## Conclusion

Explication du Code
- push : Ajoute un élément au sommet de la pile.
- pop : Retire l'élément au sommet de la pile, ou retourne None si la pile est vide.
- peek : Affiche l'élément au sommet de la pile sans le retirer.
- is_empty : Vérifie si la pile est vide.
- display : Affiche la pile actuelle.

Avec cet exemple, tu peux voir comment utiliser les opérations de base d'une stack pour stocker et gérer des données selon le principe LIFO. Les stacks sont simples, mais elles sont extrêmement utiles dans de nombreux algorithmes et applications en programmation.