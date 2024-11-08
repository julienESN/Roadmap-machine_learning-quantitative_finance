# Exercice 5 : Implémentation d’une File
# Implémenter une file avec les opérations enqueue et dequeue.

class Queue:
    def __init__(self):
        self.items = []

    # Enqueue - Ajouter un élément à la fin de la file
    def enqueue(self, item):
        self.items.append(item)
        print(f"Élément {item} ajouté à la file")

    # Dequeue - Retirer un élément du début de la file
    def dequeue(self):
        if not self.is_empty():
            dequeued_item = self.items.pop(0)
            print(f"Élément {dequeued_item} retiré de la file")
            return dequeued_item
        else:
            print("La file est vide")
            return None

    # Peek - Consulter l'élément au début de la file sans le retirer
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("La file est vide")
            return None

    # Vérifier si la file est vide
    def is_empty(self):
        return len(self.items) == 0

    # Afficher la file
    def display(self):
        print("File actuelle :", self.items)
        
        
# Exercice 6 : Simulation de File d’Attente
# Simuler une file d’attente où les clients entrent et sortent. Écrire une fonction qui calcule le temps total passé par chaque client dans la file.

def simulate_queue(customers):
    queue = Queue()
    total_time = 0
    for customer in customers:
        queue.enqueue(customer)
        total_time += len(queue.items) - 1
    return total_time
  
customers = ["Alice", "Bob", "Charlie", "David"]
total_time = simulate_queue(customers)
print(f"Temps total passé dans la file : {total_time}")
