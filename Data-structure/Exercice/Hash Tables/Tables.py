# Tables de Hachage (Hash Tables)
# Exercice 10 : Implémentation d’une Table de Hachage
# Implémenter une table de hachage avec un mécanisme de résolution des collisions (comme le chaining).

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
      
    def word_count(self, cle):
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
      
# Exemple d'utilisation

table = HashTableSeparateChaining(10)

table.inserer("foo", 42)
table.inserer("foo", 42)

table.inserer("bar", 1337)
table.inserer("baz", 7)

print(table.rechercher("foo"))  # 42
# Exercice 11 : Comptage de Mots
# Écrire une fonction qui prend une liste de mots et retourne un dictionnaire indiquant le nombre de fois où chaque mot apparaît.

def word_count(words):
    table = HashTableSeparateChaining(len(words))
    for word in words:
        count = table.word_count(word)
        if count is None:
            table.inserer(word, 1)
        else:
            table.inserer(word, count + 1)
    return table
  
# Exemple d'utilisation

words = ["foo", "bar", "baz", "foo", "bar", "foo", "baz", "foo", "qux"]

print(word_count(words).table)