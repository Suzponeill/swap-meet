import pytest


class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    #return a list of items that the vendor has in a given category  
    def get_by_category(self, category):
        category_list = []
        for item in self.inventory:
            if item.category == category:
                category_list.append(item)

        return category_list

    """
    Swap_items vendor method checks if the items are in each vendor's inventory,
    then removes and adds items from both vendor's inventories.
    """
    def swap_items(self, other_vendor, my_item, their_item):
        
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        else:
            self.remove(my_item) and other_vendor.remove(their_item)
            self.add(their_item) and other_vendor.add(my_item)
            return True