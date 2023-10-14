from linkedlist import *
from restaurantData import *


def create_types_ll(data: list):
    new_ll = LinkedList()
    for i in data:
        new_ll.insert_beginning(i)
    return new_ll


def create_restaurant_ll(data: list):
    restaurant_list = LinkedList()
    for type in types:
        for restaurant in restaurant_data:
            if restaurant[0] == type:
                restaurant_list.insert_beginning(restaurant)

    return restaurant_list
        


types_ll = create_types_ll(types)
print(types_ll.stringify_list())

restaurant_ll = create_restaurant_ll(restaurant_data)

def print_ll(ll):
    current_node = ll.get_head_node()
    while current_node:
        print(current_node.get_value().stringify_list())
        current_node = current_node.get_next_node()

# print_ll(restaurant_ll)
print(restaurant_ll.stringify_list())

