class Inventory:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items = []


    def add_item(self, item: str):
       if self.capacity > len(self.items):
           self.items.append(item)
       else:
        return "not enough room in the inventory"

    def get_capacity(self):
        return self.capacity

    def __repr__(self):
        current_capacity = len(self.items) - self.capacity
        return f"Items: {', '.join(self.items)}.\nCapacity left: {current_capacity}"

# input
inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)

"""

not enough room in the inventory
2
Items: potion, sword.
Capacity left: 0


"""