# Exercice 1 : Array Basics
# Écrire une fonction qui prend un tableau et retourne la somme de ses éléments.
import numpy as np

def sum_array(arr):
    return np.sum(arr)
  
# Test

print(sum_array([1, 2, 3, 4])) # 10

# Exercice 2 : Listes Chaînées
# Implémenter une liste chaînée simple avec des méthodes ajouter (à la fin), supprimer (par valeur), et afficher (parcours de la liste).

class Node:
    def __init__(self, valeur):
        self.valeur = valeur
        self.suivant = None

class LinkedList:
    def __init__(self):
        self.tete = None

    # Ajouter un élément à la fin de la liste
    def ajouter(self, valeur):
        nouveau_noeud = Node(valeur)
        if not self.tete:  # Si la liste est vide
            self.tete = nouveau_noeud
        else:
            courant = self.tete
            while courant.suivant:  # Parcourt jusqu'au dernier nœud
                courant = courant.suivant
            courant.suivant = nouveau_noeud  # Ajoute le nouveau nœud à la fin

    # Supprimer un nœud par valeur
    def supprimer(self, valeur):
        courant = self.tete
        precedent = None
        while courant:
            if courant.valeur == valeur:
                if precedent:  # Si le nœud n'est pas la tête
                    precedent.suivant = courant.suivant
                else:  # Si le nœud est la tête
                    self.tete = courant.suivant
                return True  # Valeur trouvée et supprimée
            precedent = courant
            courant = courant.suivant
        return False  # Valeur non trouvée

    # Afficher tous les éléments de la liste
    def afficher(self):
        courant = self.tete
        while courant:
            print(courant.valeur, end=" -> ")
            courant = courant.suivant
        print("None")  # Indique la fin de la liste

# Utilisation de la liste chaînée
ma_liste = LinkedList()
ma_liste.ajouter(10)
ma_liste.ajouter(20)
ma_liste.ajouter(30)
ma_liste.afficher()  # Sortie attendue : 10 -> 20 -> 30 -> None

ma_liste.supprimer(20)
ma_liste.afficher()  # Sortie attendue : 10 -> 30 -> None

ma_liste.supprimer(10)
ma_liste.afficher()  # Sortie attendue : 30 -> None

ma_liste.supprimer(40)  # Tentative de supprimer un élément non présent
ma_liste.afficher()  # Sortie attendue : 30 -> None
