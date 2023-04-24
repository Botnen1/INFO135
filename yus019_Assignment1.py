#Task 1
print("\n\nTask 1")
"""Suppose you’re looking for a word in the following dictionaries. In the worst case how
many steps do you think the search will take with Binary Search?"""
""" 
#A Persian
    18
#B English
    21
#C Chinese
    18 
"""

def binary(tall):
    ganger = 0
    while tall > 1:
        tall = tall/2
        ganger += 1
    print(ganger)
binary(171476)
binary(1100373)
binary(260000)
binary(262144)

#Task 2
print("\nTask 2")
""" Write a class called Student that has two following methods:
• Method 1: init() that receives name, age and country of a student and sets
them as instance variables.
• Method 2: greeting() that prints the following message for a student whose name
is Sara, 25 years old and from Norway: """

class Student:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def greeting(self):
        print("Hei, jeg heter", self.name,"\nJeg er",self.age,"år gammel \nJeg er fra", self.country)

sara = Student("Sara", 25, "Norge")
sara.greeting()

#Task 3
print("\nTask 3")
""" Given the following linked-list class, write a method called print_list() that loops
over and prints the entire contents of a linked-list starting from head. """

class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    def get_next(self):
        return self.next
    def anext(self):
        if self.get_next() is None:
            return False
        return True
    def stringer(self):
        return "Node value: "+str(self.data)

class LinkedList(object):
    def __init__(self, head = None):
        self.head = head
        self.size = 0   
    def add(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        self.size += 1
    def listeprint(self):
        print("Printing....")
        if self.head is None:
            return 
        ny_node = self.head
        print(ny_node.stringer())
        while ny_node.anext():
            ny_node = ny_node.get_next()
            print(ny_node.stringer())

def hoved():
    my_list = LinkedList()
    my_list.add(5)
    my_list.add(8)
    my_list.add(3)
    my_list.add(4)
    my_list.listeprint()

hoved()

#Task 4
print("\nTask 4")
""" Write a function reverse_list() that receives a Python list, builds a Stack with the
same elements, and prints the reversed list. """

minliste = [1, 2, 3, 4, 5]

class Stack:
    def __init__(self):
        self.elem = []
    def add2(self, element):
        self.elem.append(element)
    def remove(self):
        return self.elem.pop()
    def is_empty(self):
        return self.elem == []

def reversed(liste):
    rev = []
    stack = Stack()
    for elem in liste:
        stack.add2(elem)
    while stack.is_empty() is False:
        rev.append(stack.remove())
    print(rev)

reversed(minliste)
