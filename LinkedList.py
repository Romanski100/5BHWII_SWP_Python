import random

class ListNode:
    """Ein Knoten der einfach verketteten Liste"""
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """Einfach verkettete Liste"""
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, value):
        """Fügt ein Element am Ende der Liste hinzu"""
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def length(self):
        """Gibt die Länge der Liste zurück"""
        return self.size

    def print_list(self):
        """Gibt alle Elemente der Liste aus"""
        current = self.head
        elements = []
        while current:
            elements.append(str(current.value))
            current = current.next
        print(" -> ".join(elements))

    def __iter__(self):
        """Macht die Liste iterierbar"""
        self._iter_node = self.head
        return self

    def __next__(self):
        """Liefert das nächste Element in der Iteration"""
        if self._iter_node is None:
            raise StopIteration
        value = self._iter_node.value
        self._iter_node = self._iter_node.next
        return value

# Hauptprogramm
def main():
    linked_list = LinkedList()

    # Befüllen mit zufälligen Zahlen
    for _ in range(10):
        linked_list.append(random.randint(1, 100))

    # Ausgabe der Liste
    print("Inhalt der verketteten Liste:")
    linked_list.print_list()

    # Länge der Liste ausgeben
    print(f"Länge der Liste: {linked_list.length()}")

    # Iterator verwenden
    print("Iterieren über die Liste:")
    for value in linked_list:
        print(value, end=" ")

if __name__ == "__main__":
    main()
