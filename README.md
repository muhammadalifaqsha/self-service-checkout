# Self-Service Supermarket Mini Project

## 1. Background

The rapid development of machine learning and artificial intelligence (AI) has disrupted the way we perform our daily activities. One of them is our shopping habits in which we become increasingly adapted (even reliant) to self-service and online markets. One crucial structure to support this type of shopping activities is a reliable self-service cashier system. Consequently, it is necessary for programmers working in this sector to develop such system.

## 2. Objectives
We are going to build a simple code of self-service cashier system with the abilities to:
- Receive inputs of item (consisting of name, quantities, and price per qty)
- Edit previous inputs of item (name, quantities, or price)
- Remove some or all inputs of item
- Check whether all inputs of item are correct at the end
- Print the details of the shopping list (all items) and the price total (with a certain discount scheme)

## 3. What We Need

We are going to build a class Transaction with the following attributes and methods.

| Attribute | Data type | Description |
| :-- | :-- | :-- |
| shopping_list | Dict | A dictionary with the name of items as the keys, a list of two numbers (quantity & price) as the value |


| Method | Input | Output |
| :-- | :-- | :-- |
| add_item | Name, quantity, and price of item | Name, quantity, and price of item are added to shopping list |
| update_item_name | Previous item name | Item name is changed in the shopping list |
| update_item_qty | Item name to be edited, new quantity | Quantity of item is changed in the shopping list |
| update_item_price | Item name to be edited, new price| Price of item is changed in the shopping list |
| delete_item | Item name to be removed | Item is removed from the shopping list |
| reset_transaction |  | All items in the shopping list are removed |
| check_order |  | A table of shopping list (name, quantity, price, total price for each item) and whether the shopping list is correct or not (e.g. no item name or negative quantity/price) |
| total_price |  | The total price, discounted using a certain scheme |

## 4. Code Flow & Short Explanations

### As a whole

We are going to build a simple interface for users so that they shouldn't have to explicitly call each methods in Transaction class in order to add or edit their shopping list. 

1. while True (still wanting to shop) do
    1. show all commands to shop
    2. if user wants to add new item
        1. Input item_name, quantity, price
        2. .add_item(item_name, quantity, price)
        3. Raise a message if item specification is not suitable (e.g. quantity is not a number)
    3. if user wants to edit item name
        1. Input old_item_name, new_item_name
        2. .update_item_name(old_item_name, new_item_name)
        3. Raise a message if old_item_name is not in the shopping list 
    4. if user wants to edit the quantity of an item
        1. Input item_name, new_quantity
        2. .update_item_quantity(item_name, new_quantity)
        3. Raise a message if new_quantity is not a number or if item_name is not in the shopping list
    5. if user wants to edit the price of an item
        1. Input item_name, new_price
        2. .update_item_quantity(item_name, new_price)
        3. Raise a message if new_price is not a number or if item_name is not in the shopping list
    6. if user wants to delete an item
        1. Input item_name
        2. .delete_item(item_name)
        3. Raise a message if item_name is not in the shopping list
    7. if user wants to delete all items
        1. Raise a warning message whether the user really wants to delete all items
            1. if yes, .reset_transaction()
            2. else, pass
    8. if user wants to check the shopping list
        1. .check_order()
    9. if user wants to check price total
        1. .price_total()
    10. if user wants to stop shopping
        1. break from while loop

To make our codes cleaner, we can put the instructions of each shopping command (e.g. the instructions within the branch 'if user wants to add an item') into a function in itself (with the same name as the method used in them; there's no naming conflict as the methods are only defined in instances of Transaction)

Instead of putting the "try" and "except" cases in the methods, we put it inside the function/branch of shopping command above (e.g. on the instructions within the branch 'if user wants to add an item').

The code flow & explanation for each method in class Transaction is as follows.

### .add_item()

This method adds a new item into the object attribute .shopping_list, a dictionary with item names as keys, and their quantity and prices as values. 

1. Input: item_name, item_qty, item_price
2. Append item_name: [item_qty, item_price] into .shopping_list

### .update_item_name()

This method edits an item name in .shopping_list.

1. Input: old_item_name, new_item_name
2. Find old_item_name in .shopping_list, save the value [item_qty, item_price] temporarily
3. Pop old_item_name from .shopping_list
4. Add new_item_name as key to .shopping_list with previously saved value [item_qty, item_price]

### .update_item_qty()

This method edits the quantity of an item in .shopping_list

1. Input: item_name, new_qty
2. Find item_name in .shopping_list
3. Change the first entry of the value into new_qty

### .update_item_price()

This method edits the price of an item in .shopping_list

1. Input: item_name, new_price
2. Find item_name in .shopping_list
3. Change the second entry of the value into new_price

### .delete_item()

This method deletes an item from .shopping_list

1. Input: item_name
2. Find item_name in .shopping_list
3. Pop said item_name from .shopping_list

### .reset_transaction

This method changes .shopping_list into an empty dictionary

1. Input: -
2. Change .shopping_list into an empty dictionary

### .check_order

This method prints out a tabulated version of .shopping_list (plus the total price for each item). If .shopping_list contains empty string or whitespace as one of its keys, or if it contains a non-positive number as one of its values, then a warning message "Your transaction contains mistakes" is also printed out.

1. Input: -
2. Tabulate & print the data on the shopping list, including the total price of each item (item_qty * item_price)
3. If one of the keys in .shopping_list is empty string or whitespace, or one of the values includes a non-positive number, print a warning message: "Your transaction contains mistakes"

### .total_price

This method calculate the total price of orders, discounted using a certain scheme.

1. Input: -
2. Multiply the two numbers in each value of .shopping_list, then sum them all into a variable (total)
3. If total <= 200,000, discount_rate = 0
4. Else if total <= 300,000, discount_rate = 0.05
5. Else if total <= 500,000, discount_rate = 0.08
6. Else, discount_rate = 0.1
7. Return final_total = (1-discount_rate) * total

## 5. Demo

### Test 1

We are going to add two items: Ayam Goreng (qty: 2, price: Rp20,000.0) and Pasta Gigi (qty: 3, price: Rp15,000.0) one-by-one. 

<img src="https://github.com/muhammadalifaqsha/self-service-checkout/blob/main/Screenshots/Test1.png?raw=true" width="500">

As we might see, we've successfully added the two items.

### Test 2

We are going to remove Pasta Gigi item from our shopping cart.

<img src="https://github.com/muhammadalifaqsha/self-service-checkout/blob/main/Screenshots/Test2.png?raw=true" width="500">

We've successfully deleted it.

### Test 3

We are going to reset our transaction.

<img src="https://github.com/muhammadalifaqsha/self-service-checkout/blob/main/Screenshots/Test3.png?raw=true" width="500">

Our shopping cart is now empty.

### Test 4

Suppose we've added back those two items, Ayam Goreng (qty: 2, price: Rp20,000.0) and Pasta Gigi (qty: 3, price: Rp15,000.0), with the addition of Mainan Mobil (qty: 1, price: Rp200,000.0) and Mi Instan (qty: 5, price: Rp3,000.0). Now we're going to check the total of our orders.

<img src="https://github.com/muhammadalifaqsha/self-service-checkout/blob/main/Screenshots/Test4.png?raw=true" width="500">

Our shopping list totals to Rp285,000.0, including a discount of 5% (because our undiscounted total is larger than Rp200,000.0 but still no larger than Rp300,000.0 to get the 8% discount rate).

### Bonus Test 5a

We may also look at the tabulated shopping list as follows.

<img src="https://github.com/muhammadalifaqsha/self-service-checkout/blob/main/Screenshots/Test5a.png?raw=true" width="500">

### Bonus Test 5b

Suppose we add a '' (emptystring) item into the shopping list, and proceed to check our orders.

<img src="https://github.com/muhammadalifaqsha/self-service-checkout/blob/main/Screenshots/Test5b.png?raw=true" width="500">

Now a warning message "Your transaction contains mistakes!" appears because our cart contains an item with '' (emptystring) name.


## 6. Conclusions
