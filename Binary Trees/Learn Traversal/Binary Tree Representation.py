# Binary Tree Representation

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

r"""
       Drinks
        /   \
      Hot   Cold
     / \    /  \
   Coffee Tea Cola Fanta
"""

drinks = Node("Drinks")
Hot = Node("Hot")
Cold = Node("Cold")
Coffee = Node("Coffee")
Tea = Node("Tea")
Cola = Node("Cola")
Fanta = Node("Fanta")

drinks.left = Hot
drinks.right = Cold
Hot.left = Coffee
Hot.right = Tea
Cold.left = Cola
Cold.right = Fanta

print(drinks.left.right.val)  # Tea
