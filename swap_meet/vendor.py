import pytest


class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            inventory = []
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

    """
    swap_first_item function 
    """

    def swap_first_item(self, other_vendor):
        if len(self.inventory) == 0 or len(other_vendor.inventory) ==0:
            return False

        self.add(other_vendor.inventory[0])
        other_vendor.add(self.inventory[0])
        self.remove(self.inventory[0])
        other_vendor.remove(other_vendor.inventory[0])
        return True
    
    """
    get_best_by_category class method returns the item with the best condiiton filtered by the category argument
    """
    
    def get_best_by_category(self, category):
        #leverage the get_by_category method to get a list of inventory items in the given category
        category_list = self.get_by_category(category)
        
        #iterate through list of items to find best condition 
        max_condition = 0.0
        for item in category_list:
            if item.condition > max_condition:
                max_condition = item.condition
        
        #iterate through the category list again to find the best item 
        for item in category_list:
            if item.condition == max_condition:
                return item

    """
    swap_best_by_category method
    """
    def swap_best_by_category(self, other, my_priority, their_priority):
        #use len of get_by_category to return false if either vendor does not have the other's preference
        if len(self.get_by_category(their_priority)) == 0 or len(other.get_by_category(my_priority)) == 0:
            return False
        
        #use get_best_by_category to assign variables to each item to swap
        their_item = other.get_best_by_category(my_priority)
        my_item = self.get_best_by_category(their_priority)

        #use swap_items to move the items between the vendors
        self.swap_items(other, my_item, their_item)
        return True


