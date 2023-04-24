""" Assignment 2 """
#Advanced Programming 
# (INFO135)
"""yus019@uib.no"""

#oppgave1
print("\nOppgave 1")
""" 1. Suppose you have the following list of numbers to sort:
[ 1001, 1030, 1050, 1020, 300, 1080, 1100]
 What will be the partially sorted list after 3 passes of Selection Sort? """

numbers = [1001, 1030, 1050, 1020, 300, 1080, 1100]

def finn_minste(liste):
    minste = liste[0]
    laveste = 0
    for i in range(1,len(liste)):
        if liste[i] < minste:
            minste = liste[i]
            laveste = i
        return laveste

def selection_sort(liste):
    ny_liste = []
    for i in range(0,3):
        minste = finn_minste(liste)
        ny_liste.append(liste.pop(minste))
    return ny_liste



numbers_sorted = selection_sort(numbers)
print(numbers_sorted)

#[1001, 1030, 1020]


#oppgave2
print("\nOppgave 2")
"""  2. Suppose you have the following list of numbers to sort:
[ 210, 15, 111, 90, 45, 120, 150, 200, 100, 140 ]
 What will be the partially sorted list after 3 passes of Bubble Sort? """
 
def bubble_sort(liste):
    antall = 0
    for pass_num in range(len(liste) - 1, 0, -1):
        while antall < 3:
            antall += 1
            for i in range(pass_num):
                if liste[i] > liste[i + 1]:
                    temp = liste[i]
                    liste[i] = liste[i + 1]
                    liste[i + 1] = temp
                    

numbers = [210, 15, 111, 90, 45, 120, 150, 200, 100, 140]

print(bubble_sort(numbers))
print(numbers)

#[15, 45, 90, 111, 120, 100, 140, 150, 200, 210]


#oppgave3
print("\nOppgave 3")
""" 3. Write a function called sort_and_rem_dup() that receives a list of numbers and
returns a sorted list where the duplicates in the numbers are removed. """


def finn_minste(liste):
    minste = liste[0]
    laveste = 0
    for i in range(1,len(liste)):
        if liste[i]<minste:
            minste = liste[i]
            laveste = i
    return laveste

def sort_and_rem_dump(liste):
    new_array = []
    for i in range(len(liste)):
        minste = finn_minste(liste)
        a = array.pop(minste)
        if a not in new_array:
            new_array.append(a)
    return new_array  

array = [5, 4, 3, 2, 1, 2, 3, 4, 5]
newlist = sort_and_rem_dump(array)
print(newlist)


#oppgave4
print("\nOppgave 4")
""" 4. Write a function check_palindrome(word) that receives a string variable called
word as an input parameter, and builds a Stack and a Queue where their elements are the
letters (characters) of that word. Then, the function should check and print if the word is
a Palindrome or not.  """


class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()

stack = Stack()
tekst = input("String:").lower()
 
for x in tekst:
    stack.push(x)
 
reversert = ""
while not stack.is_empty():
    reversert = reversert + stack.pop() #Legger tegnene fra input inn i den tomme strengen "reversert"
 
if tekst == reversert: #Sjekker om "reversert", er identisk til den orginale inputen
    print("Palindrom")
        #True
else:
    print("Ikke Palindrom")
        #False
