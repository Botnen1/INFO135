""" Assignment 5 """
#Advanced Programming 
# (INFO135)


#Oppgave1
print("\nOppgave 1")
""" Which of the following Trees are Full Binary Tree. """
#Binary Tree 1
#Binary Tree 2
#Binary Tree 3
print("They are all full binary trees")


#Oppgave2
print("\nOppgave 2")
"""Use the implementation of Binary Tree (based on List of Lists) provided in Lectures and
write a function called make_tree() that builds the following tree and prints it in the output."""


def binary_tree(r):
    return [r, [], []]

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]

def insert_left_child(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root

def insert_right_child(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])
    return root


def make_tree():
    tre = binary_tree(1)
    insert_left_child(tre, 2)
    insert_right_child(tre, 3)

    insert_left_child(get_left_child(tre), 4)
    insert_right_child(get_right_child(tre), 5)
    insert_right_child(get_right_child(tre), 6)
    
    return tre

print(make_tree())


#Oppgave3
print("\nOppgave 3")
""" Write a function build_my_graph2() that:
    a) creates the following Graph.
    b) runs Depth First Search (DFS) algorithm starting 
        from node ‘a’ and prints all the visited nodes.
What is printed in the output when you run the function? """


class Graph:
    graph = dict()
    searched = []
    


    def add_edge(self, node, neighbour):
            if node not in self.graph:
                self.graph[node] = [neighbour]

            else: 
                self.graph[node].append(neighbour)

    def depth_first_search(self, node):
        if node not in self.searched:
            print("[",node, end ="],")
            
            self.searched.append(node)
            if node in self.graph:
                for neighbour in self.graph[node]:
                    self.depth_first_search(neighbour)
        """ print(self.searched) """

    
def build_my_graph2():
    min_graf = Graph()

    min_graf.add_edge("a", "b")
    min_graf.add_edge("a", "c")
    min_graf.add_edge("b", "c")
    min_graf.add_edge("b", "d")
    min_graf.add_edge("c", "e")
    min_graf.add_edge("d", "e")
    min_graf.add_edge("e", "f")
    min_graf.add_edge("f", "c")
    min_graf.add_edge("d", "g")
    min_graf.add_edge("d", "h")

    min_graf.depth_first_search("a")
    
build_my_graph2()

    
#Oppgave4
print("\n\nOppgave 4")
"""Use the Binary Search Tree (BST) class (provided in Lecture notes) and write two new
methods that are described in the following:
a) compute_sum() that computes the sum of all the node values in the BST
b) compute_count() that computes the total number of nodes """


        
class BinarySearchTree:

    def __init__(self, verdi = None):
        self.verdi = verdi
        if self.verdi:
            self.left_child = BinarySearchTree()
            self.right_child = BinarySearchTree()
        else:
            self.left_child = None
            self.right_child = None
    
    def is_empty(self):
        return self.verdi is None

    def insert(self, verdi):
        if self.is_empty():
            self.verdi = verdi
            self.left_child = BinarySearchTree()
            self.right_child = BinarySearchTree()

        elif verdi < self.verdi:
            self.left_child.insert(verdi)
        elif verdi > self.verdi:
            self.right_child.insert(verdi)


    def compute_sum(self):
        if self.verdi is None:
            return False        
        else:
            return self.verdi + self.left_child.compute_sum() + self.right_child.compute_sum()

    def compute_count(self):
        if self.verdi is None:
            return False
        else:
            return 1 + self.left_child.compute_count() + self.right_child.compute_count()

    

tre = BinarySearchTree()
tre.insert(2)
tre.insert(4)
tre.insert(6)
tre.insert(8)
tre.insert(10)

""" print(tre) """
print("sum:", tre.compute_sum())
print("number of nodes:", tre.compute_count())



