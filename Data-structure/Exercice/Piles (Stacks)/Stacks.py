# Exercice 3 : Implémentation d’une Pile
# Implémenter une pile avec les opérations push, pop, et peek. Écrire une fonction qui utilise la pile pour vérifier si une chaîne de caractères est un palindrome (ex. "radar").

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

def is_palindrome(string):
    stack = Stack()
    for char in string:
        stack.push(char)
    reversed_string = ""
    print("Reversing the string")
    while not stack.is_empty():
        reversed_string += stack.pop()
    return string == reversed_string
  
is_palindrome("radar") # True      

# Exercice 4 : Vérification de Parenthèses
# Écrire une fonction qui utilise une pile pour vérifier si une chaîne contenant des parenthèses est bien formée, par exemple (a + b) * (c + d).

def is_balanced(expression):
    stack = Stack()
    for char in expression:
        if char in ["(", "{", "["]:
            stack.push(char)
        elif char in [")", "}", "]"]:
            if stack.is_empty():
                return False
            if (char == ")" and stack.peek() == "(") or (char == "}" and stack.peek() == "{") or (char == "]" and stack.peek() == "["):
                stack.pop()
            else:
                return False
    return stack.is_empty()
  
is_balanced("(a + b) * (c + d)") # True