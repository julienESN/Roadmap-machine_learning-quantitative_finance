# Exercice 7 : Parcours d’Arbre
# Implémenter un arbre binaire et écrire des fonctions pour les parcours en profondeur (in-order, pre-order, post-order).
 
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
    
    # Calcul de la hauteur de l'arbre
    def _hauteur_recursif(self, noeud):
        if noeud is None:
            return -1
        hauteur_gauche = self._hauteur_recursif(noeud.gauche)
        hauteur_droit = self._hauteur_recursif(noeud.droit)
        return 1 + max(hauteur_gauche, hauteur_droit)
      
    def hauteur(self):
        return self._hauteur_recursif(self.racine)
          

    # Affichage en ordre croissant (parcours en ordre)
    def parcours_en_ordre(self):
        self._parcours_en_ordre_recursif(self.racine)

    def _parcours_en_ordre_recursif(self, noeud):
        if noeud is not None:
            self._parcours_en_ordre_recursif(noeud.gauche)
            print(noeud.valeur, end=" ")
            self._parcours_en_ordre_recursif(noeud.droit)


BST = BST()
BST.inserer(10)
BST.inserer(5)
BST.inserer(15)
BST.inserer(2)
BST.inserer(7)
BST.inserer(12)
BST.inserer(17)
BST.parcours_en_ordre() # 2 5 7 10 12 15 17
print("\nHauteur de l'arbre :", BST.hauteur())  # Appel à la méthode publique `hauteur`
print("Recherche de 12 :", BST.rechercher(12))  # Sortie attendue : True

# Exercice 8 : Arbre Binaire de Recherche
# Implémenter un arbre binaire de recherche (BST) avec les opérations insert, search, et delete.
# Exercice 9 : Hauteur d’un Arbre
# Écrire une fonction qui calcule la hauteur d’un arbre binaire.

    # Calcul de la hauteur de l'arbre
      