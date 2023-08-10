import json
import os

menu=None
sales=None
currentOrder=None

script_dir = os.path.dirname(os.path.abspath(__file__))

menu_path = os.path.join(script_dir, 'menu.json')
sales_path = os.path.join(script_dir, 'sales.json')
currentOrder_path = os.path.join(script_dir, 'currentOrder.json')

with open (menu_path,"r") as json_file:
    menu = json.load(json_file)

with open(sales_path,"r") as json_file:
    sales=json.load(json_file)

with open(currentOrder_path,"r") as json_file:
    currentOrder=json.load(json_file)

def saveData(filename,data):
    with open (filename,"w") as json_file:
        json.dump(data,json_file,indent=4)
        displayMenu()
      

def displayMenu():
    print("\nMenu:")
    print("{:<5} {:<15} {:<10} {:<10}".format("ID", "Dish name", "Price", "Availability"))
    print("=" * 60)
    
    for item in menu.values():
      availability = "Available" if item['availability'] else "UnAvailable" if item['availability'] == False else "Out of Stock"

      print("{:<5} {:<15} {:<10} {:<10}".format(item['id'], item['name'], item['price'], availability))


def addItemInMenu(name,price):
    menu[len(menu)+1]={"id":len(menu)+1,"name":name,"price":price,"availability":True}
    saveData(menu_path,menu)

def deleteItemInMenu(id):
    id_str = str(id)
    if id_str in menu:  
      del menu[id_str] 
    saveData(menu_path,menu)

def updateAvailabilityInMenu(id):
    menu[id]["availability"] = not menu[id]["availability"]
    saveData(menu_path,menu)

def orderDish(order,name,price):
    latestOrder= {
            "id":int(len(currentOrder["order"])+1),
            "customer_name": name,
            "ordered_dishes":[order],
            "price":price,
            "status": "received"
        }
    print("\n Your total is : ",price)
    currentOrder["order"].append(latestOrder)
    saveData(currentOrder_path,currentOrder)


def updateOrder(id):
    for order in currentOrder["order"]:
        if order["id"] == int(id) :
            if order["status"] == "received":
                order["status"] = "preparing"
            elif order["status"] == "preparing":
                 order["status"] = "pickup"
            elif order["status"] == "pickup":
                 order["status"] = "delivered"
                 sales["sales"].append(order)
            else : print("\nOrder already delivered")

        saveData(currentOrder_path,currentOrder)

while True:
    print("\n 1 : Check Menu")
    print(" 2 : Add a dish")
    print(" 3 : Remove a dish")
    print(" 4 : update Availability ")
    print(" 5 : Order a Disk ")
    print(" 6 : Update Order")
    choice=input("\nplease Enter your choice : ")
    print(choice)

    if choice == "1" :
        displayMenu()
    elif choice =="2" :
        name = input("\nPlease Enter Dish Name : ")
        price = input("please enter price : ")
        addItemInMenu(name,price)
    elif choice == "3" :
        id = input("\nPlease enter id : ")
        deleteItemInMenu(id)
    elif choice == "4" :
        id = input("\nPlease enter id : ")
        updateAvailabilityInMenu(id)
    elif choice == "5" :
        name = input("Please Enter your Name : ")
        order = []
        while True :
           id = input("\nPlease enter id : ")
           quantity = input("\nPlease enter quantity: ")
           ordering = input("\nAre you wanna add any other dish yes/no : ")
          
           existing_dish = next((dish for dish in order if dish["dish_id"] == id), None)

           if existing_dish :
               existing_dish["quantity"]+=int(quantity)
           else:
            order.append({
                    "dish_id": id,
                    "quantity": int(quantity),
                    })
        
           if ordering == "no":
               price=0
               for item in order:
                   price += menu[item["dish_id"]]["price"]*int(item["quantity"]) 

               orderDish(order,name,price)
               break
    elif choice == "6" :
        id = input("\nPlease enter id : ")
        updateOrder(id)