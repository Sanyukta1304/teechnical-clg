class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head

    def display(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")

    def length(self):
        if not self.head:
            return 0
        count = 0
        temp = self.head
        while True:
            count += 1
            temp = temp.next
            if temp == self.head:
                break
        return count

    def search(self, key):
        if not self.head:
            return False
        temp = self.head
        while True:
            if temp.data == key:
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False

    def delete(self, key):
        if not self.head:
            return
        current = self.head
        prev = None
        while True:
            if current.data == key:
                if prev:
                    prev.next = current.next
                else:
                    temp = self.head
                    while temp.next != self.head:
                        temp = temp.next
                    if self.head == self.head.next:
                        self.head = None
                        return
                    temp.next = self.head.next
                    self.head = self.head.next
                return
            prev = current
            current = current.next
            if current == self.head:
                break

if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.append(1)
    cll.append(2)
    cll.append(3)
    cll.display()
    print("Length:", cll.length())
    print("Search 2:", cll.search(2))
    cll.delete(2)
    cll.display()
    print("Search 2 after delete:", cll.search(2))
