# Define the item information
item1 = {
    'Item Name': 'Milk',
    'Quantity': 2,
    'Price': 2.50
}

# Create a list of items
shopping_list = [item1]

# Print the initial shopping list
print('Initial Shopping List:', shopping_list)

# Add three more items to the shopping list
item2 = {'Item Name': 'Eggs', 'Quantity': 12, 'Price': 3.00}
item3 = {'Item Name': 'Bread', 'Quantity': 1, 'Price': 2.00}
item4 = {'Item Name': 'Butter', 'Quantity': 1, 'Price': 1.50}

shopping_list.append(item2)
shopping_list.append(item3)
shopping_list.append(item4)

print('Shopping List after adding items:', shopping_list)

# Remove one item from the shopping list
shopping_list.remove(item3)

print('Shopping List after removing an item:', shopping_list)

# Change the quantity of one of the items on the shopping list
shopping_list[1]['Quantity'] = 2

print('Final Shopping List:', shopping_list)
