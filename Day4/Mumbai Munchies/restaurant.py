import json
import os

inventory=None
sales=None

script_dir = os.path.dirname(os.path.abspath(__file__))
inventory_path = os.path.join(script_dir, 'inventory.json')
sales_path = os.path.join(script_dir, 'sales.json')

with open(inventory_path, 'r') as json_file:
        data = json.load(json_file)
        inventory=data

with open(sales_path, 'r') as json_file:
        data = json.load(json_file)
        sales=data

def display_inventory():
    print("\nCurrent Snack Inventory:")
    print("{:<5} {:<15} {:<10} {:<10} {:<10}".format("ID", "Snack", "Price", "Stocks", "Availability"))
    print("=" * 60)
    
    for item in inventory.values():
      availability = "Available" if item['availability'] else "UnAvailable" if item['availability'] == False else "Out of Stock"

      print("{:<5} {:<15} {:<10} {:<10} {:<10}".format(item['id'], item['snack'], item['price'], item['stocks'], availability))

def display_Sales():
    print("\nCurrent Sales:")
    print("{:<15} {:<15} {:<10} {:<10}".format("Snack", "Price", "Quantity", "Amount"))
    print("=" * 60)
    
    for item in sales.values():
      print("{:<15} {:<15} {:<10} {:<10}".format(item['snack'], item['price'], item['quantity'], item['amount']))




def save_inventory():
    with open(inventory_path, "w") as file:
        json.dump(inventory, file, indent=4)

def save_sales():
    with open(sales_path, "w") as file:
        json.dump(sales, file, indent=4)

def addSnack(id,snack,price,stocks):
      availability = True if int(stocks) > 0 else "False"
      inventory[id]={"id":id,"snack":snack,"price":price,"stocks":stocks,"availability":availability}
      save_inventory()
      
def removeSnack(id):
     del inventory[id]
     save_inventory()
     
def updateAvailability(id):
    if id in inventory:
        inventory[id]["availability"] = not inventory[id]["availability"]
        save_inventory()


def orderSnack(id,quantity):
    if id in inventory:
        if inventory[id]["availability"] and inventory[id]["stocks"] >= int(quantity):
            sales[len(sales)+1] = {
                    "snack": inventory[id]["snack"],
                    "price":inventory[id]["price"],
                    "quantity": quantity,
                    "amount": int(inventory[id]["price"]) * int(quantity)
                }

            inventory[id]["stocks"] = int(inventory[id]["stocks"] - int(quantity))
            save_inventory()
            save_sales()
            print("Sale recorded.")
        else:
            print("Snack not available for sale.")
    else:
        print("Snack not found in inventory.")

     

while True:
     print("\nChoose an option:")
     print("1. Display Menu")
     print("2. Add Snack")
     print("3. Remove Snack")
     print("4. Update Availability")
     print("5. Order Items")
     print("6. check Sales")
     print("7. Exit")
     choice=input("please choose : ")
     
     if choice =="1":
          display_inventory()

     elif choice =="2":
           id=input("please tell id : ")
           snack=input("please add snack name : ")
           price=input("please add price : ")
           stocks=input("please add stocks : ")
           addSnack(id,snack,price,stocks)
           print("\nSnacks added successfully")

     elif choice=="3":
          id=input("please tell id : ")
          removeSnack(id)
          display_inventory()
     elif choice=="4":
          id=input("please tell id : ")
          updateAvailability(id)
          display_inventory()
     elif choice == "5":
          id=input("please tell id : ") 
          quantity=input("please tell quantity : ")
          orderSnack(id,quantity)
     elif choice == "6":
          display_Sales()
     elif choice =="7":
           print("\n complete program.")
           break
        




