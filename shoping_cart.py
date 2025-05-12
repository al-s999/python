#!/bin/python3

import math
import os
import random
import re
import sys



class Item:
    # Implement the Item here
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:
    # Implement the ShoppingCart here
    def __init__(self):
        self.items = []  # Initialize an empty list to hold items in the cart

    def add(self, item):
        self.items.append(item)  # Add the item to the cart

    def total(self):
        return sum(item.price for item in self.items)  # Calculate the total price of items in the cart

    def __len__(self):
        return len(self.items)  # Return the number of items in the cart
    
if __name__ == '__main__':

    n = int(input())
    items = []
    for _ in range(n):
        name, price = input().split()
        item = Item(name, int(price))
        items.append(item)

    cart = ShoppingCart()

    q = int(input())
    for _ in range(q):
        line = input().split()
        command, params = line[0], line[1:]
        if command == "len":
            print(str(len(cart)) + "\n")
        elif command == "total":
            print(str(cart.total()) + "\n")
        elif command == "add":
            name = params[0]
            item = next(item for item in items if item.name == name)
            cart.add(item)
        else:
            raise ValueError("Unknown command %s" % command)

