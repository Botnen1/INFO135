#Assignment 3. INFO135

#   1. What is the printed output of the following code snippet?

def hash_function(input_string, size):
    total = 0
    length = len(input_string)
    for pos in range(length):
        total = total + ord(input_string[pos]) + length
    return total % size


my_list = ["alb2c3", "CiTiBnk", "232323", "myLaptop"]
my_choice = 19

for item in my_list:
    print(hash_function(item, my_choice), end=" ")


#Answer:
# The output of the code snippet is: 7 9 16 6 






#   2. Write a class HashClass...
print()
print()
import hashlib as hl
from itertools import permutations
from random import randint

class HashClass:

    def __init__(self, id_num):
        self.id_num = id_num =str(id_num)
        self.hash = self.hash_it(id_num)
        
    def hash_it(self, id_num):
        salt = str(randint(1,1000))
        self.id_num = self.id_num 
        self.hash = hl.sha1(id_num.encode()+salt.encode()).hexdigest()
        return self.hash

    def print_it(self):
        print(self.hash)


my_hash = HashClass(11011999)
my_hash.print_it()








#   3. IMDB oppgave...
print()
list_of_tuples = [("Birds of prey", 97.1), ("Dolittle", 175.0), ("The Gentlemen", 7.0), ("Falling", 22.0)]

def sort_and_print(arr):
    arr.sort(key=lambda y: y[1])
    return arr[-1]

print(sort_and_print(list_of_tuples))








print()
#   4. Write a “recursive” function called magic_function() that receives as input a string
#   variable and computes and returns a list of all permutations of a given input

def magic_function(ord):
    if len(ord) <= 1:
        return [ord]
    permutation = magic_function(ord[1:])
    bokstav = ord[0]
    res = []
    for x in permutation:
        for i in range(len(x)+1):
            res.append(x[:i] + bokstav + x[i:])
    return res

resultat = magic_function("abcd")
print(resultat)

