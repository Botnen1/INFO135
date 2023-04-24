


"""Oblig 4 INFO 135"""
#YUS019

#Task 1
print("\nTask 1\n")
#Given the following Graph, which set represents the Edge set of the Graph?

answer1 = "b)\n{ (A,B), (B,C), (B,D), (C,A), (D,A) }"
print(answer1)


#Task 2
print("\nTask 2\n")
#Extend the implementation of the solver for the N-queen problem....


COLUMNS = "abcde"
NUM_QUEENS = len(COLUMNS)
ACCEPT = 1
CONTINUE = 2
ABANDON = 3
all_solutions = []


def solve(partial_sol):
    exam = examine(partial_sol)
    if exam == ACCEPT:
        print(partial_sol)
    elif exam != ABANDON:
        for p in extend(partial_sol):
            solve(p)

def extend(partial_sol):
    results = []
    row = len(partial_sol) + 1
    for column in COLUMNS:
        new_solution = list(partial_sol)
        new_solution.append(column + str(row))
        results.append(new_solution)
    return results

def attacks(p1, p2):
    column1 = COLUMNS.index(p1[0]) + 1
    row1 = int(p1[1])
    column2 = COLUMNS.index(p2[0]) + 1
    row2 = int(p2[1])
    return (row1 == row2 or
            column1 == column2 or
            abs(row1-row2) == abs(column1-column2))

def examine(partial_sol):
    for i in range(len(partial_sol)):
        for j in range(i + 1, len(partial_sol)):
            if attacks(partial_sol[i], partial_sol[j]):
                return ABANDON
    if len(partial_sol) == NUM_QUEENS:
        return ACCEPT
    else:
        return CONTINUE


def is_solution(candidate_solution):
    res = examine(candidate_solution)
    if res == ACCEPT:
        return "Valid!"
    else:
        return "Invalid"        

    


candidate_solution1 = ['d3', 'c1', 'e5', 'b4', 'a2']
candidate_solution2 = ['e4', 'a1', 'c5', 'd2', 'b1']
result1 = is_solution(candidate_solution1)
result2 = is_solution(candidate_solution2)

print("Candidate Solution 1:", result1)
print("Candidate Solution 2:", result2)



#Task 3
print("\nTask 3\n")
#Cycle in a Graph is a path that starts from a vertex....

class Graph:
    graph = dict()
    searched = []

    def add_edge(self, node, neighbour):
        if node not in self.graph:
            self.graph[node] = [neighbour]
        else:
            self.graph[node].append(neighbour)

    def find_cycle(self, node):
        s = [node]
        queue = [node]

        while queue:
            node = queue.pop(0)

            if node in self.graph:
                for neighbour in self.graph[node]:
                    if neighbour not in s:
                        s.append(neighbour)
                        queue.append(neighbour)
                    elif neighbour in s:
                        return "The graph is cyclic!"
        return "The graph is NOT cyclic"


my_graph = Graph()
my_graph.add_edge("A", "B")
my_graph.add_edge("B", "D")
my_graph.add_edge("C", "B")
my_graph.add_edge("C", "J")
my_graph.add_edge("D", "E")
my_graph.add_edge("D", "F")
my_graph.add_edge("E", "C")
my_graph.add_edge("E", "G")
my_graph.add_edge("F", "H")
my_graph.add_edge("G", "I")

resultat = my_graph.find_cycle("A")
print(resultat)