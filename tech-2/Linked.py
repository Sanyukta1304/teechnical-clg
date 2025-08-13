class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def length(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def search(self, key):
        current_node = self.head
        while current_node:
            if current_node.data == key:
                return True
            current_node = current_node.next
        return False

    def delete(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            return
        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next
        if current_node:
            prev.next = current_node.next

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.display()
    ll.delete(2)
    ll.display()
    print("Length:", ll.length())
    print("Search 2:", ll.search(2))
