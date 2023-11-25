# CREATING NODE CLASS.
# CodeWithSalman
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
# CREATING LINKEDLIST CLASS.
class Linkedlist:
    # INITIALLY SETTING HEAD TO NONE.
    def __init__(self):
        self.head = None
    # ADDING DATA AT THE START USING PREPEND FUNCTION.
    def prepend(self, data):
        # CREATING NODE.
        new_Node = Node(data)
        new_Node.next = self.head
        if self.head:
            self.head.prev = new_Node
        self.head = new_Node
    # ADDING DATA AT THE END USING APPEND FUNCTION.
    def append(self, data):
        # CREATING NODE.
        new_Node = Node(data)
        if self.head is None:
            self.head = new_Node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_Node
        new_Node.prev = current
    # INSERTING NODE AT SPECIFIC POSITION.
    def insert(self, data, pos):
        # CREATING NODE.
        new_Node = Node(data)
        if self.head is None:
            new_Node.next = self.head
            if self.head:
                self.head.prev = new_Node
            self.head = new_Node
        current = self.head
        for i in range(pos - 1):
            if current is None:
                return
            current = current.next
        new_Node.next = current.next
        new_Node.prev = current
        if current.next:
            current.next.prev = new_Node
        current.next = new_Node
    # UPDATING NODE VALUE.
    def update(self, old, new):
        current = self.head
        while current:
            if current.data == old:
                current.data = new
                return
            current = current.next
    # SEARCHING FOR A VALUE.
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                print("Value Found")
                return
            current = current.next
    # DELETE FUNCTION TO DELETE SPECIFIC VALUE.
    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            if self.head.next:
                self.head.next.prev = None
            self.head = self.head.next
        current = self.head
        while current.next:
            if current.next.data == data:
                if current.next.next:
                    current.next.next.prev = current
                current.next = current.next.next
            current = current.next
    # DISPLAY DATA IN FORWARD DIRECTION.
    def display_Forward(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    # DISPLAY DATA IN BACKWARD DIRECTION.
    def display_Backward(self):
        current = self.head
        while current and current.next:
            current = current.next
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

# MAIN CODE OR DRIVER CODE OR MAIN FUNCTION.
# CREATING OBJECT OF THE LINKEDLIST CLASS.
# HERE LinkedList IS OBJECT NAME. U CAN GIVE ANY NAME TO THE OBJECT.
Linkedlist = Linkedlist()
while True:
    print("1 = Add Node at the End")
    print("2 = Add Node at the Start")
    print("3 = Display Nodes")
    print("4 = Insert Node at Position")
    print("5 = Update Node Value")
    print("6 = Search Node Value")
    print("7 = Delete Node")
    print("8 = Exit")
    # NOW LET'S ASK FOR USER SELECTION.
    selection = int(input("Make any One Selection from Above: "))
    if selection == 1:
        number = int(input("Enter the Number: "))
        # CALLING APPEND FUNCTION HERE TO ADD NODE AT THE END.
        Linkedlist.append(number)
        Linkedlist.display_Forward()
        Linkedlist.display_Backward()
    elif selection == 2:
        number = int(input("Enter the Number: "))
        # CALLING PREPEND FUNCTION HERE TO ADD NODE AT THE START.
        Linkedlist.prepend(number)
        Linkedlist.display_Forward()
        Linkedlist.display_Backward()
    elif selection == 3:
        # CALLING DISPLAY FUNCTION TO DISPLAY ALL THE NODES.
        Linkedlist.display_Forward()
        Linkedlist.display_Backward()
    elif selection == 4:
        # CALLING INSERT FUNCTION TO INSERT VALUE TO SPECIFIC POSITION.
        number = int(input("Enter the Number: "))
        position = int(input("Enter the Position: "))
        position -= 1
        Linkedlist.insert(number, position)
        print(position)
        Linkedlist.display_Forward()
        Linkedlist.display_Backward()
    elif selection == 5:
        # CALLING UPDATE FUNCTION HERE TO UPDATE DATA.
        Linkedlist.display_Forward()
        Linkedlist.display_Backward()
        old = int(input("Enter the Old Value: "))
        new = int(input("Enter the New Value: "))
        Linkedlist.update(old, new)
        Linkedlist.display_Forward()
        Linkedlist.display_Backward()
    elif selection == 6:
        # CALLING SEARCH FUNCTION HERE TO SEARCH FOR SPECIFIC DATA.
        Linkedlist.display_Forward()
        Linkedlist.display_Backward()
        value = int(input("Enter the value to Search: "))
        Linkedlist.search(value)
    elif selection == 7:
        # CALLING SEARCH FUNCTION HERE TO SEARCH FOR SPECIFIC DATA.
        Linkedlist.display_Forward()
        Linkedlist.display_Backward()
        value = int(input("Enter the value to Delete: "))
        Linkedlist.delete(value)
        Linkedlist.display_Forward()
        Linkedlist.display_Backward()
    elif selection == 8:
        exit()
    else:
        print("Selection out of Range")
