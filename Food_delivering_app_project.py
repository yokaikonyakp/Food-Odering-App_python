
print("Welcom to KONYAK's Restaurant.")
print("We promise you the best experience here. Have Fun !")
import random

#defining the class 
class FOODITEM:
    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = random.randint(1000, 9999)
        self.name = name
        self.quantity = quantity
        self.price = price
        self.stock = stock
        self.offer = discount
        


#defining the Admin class
class Admin:
    def __init__(self):
        self.food_items = []     #constructor "self.food_items = []" is assuming as empty list, when admin add fooditems it will be stored here




    #defining the function to add food items 
    def adding_food_items (self, name, quantity, price, discount, stock):
        food_item = FOODITEM(name, quantity, price, discount, stock)
    #appending the "FOODITEM" object to the "food_items" list 
        self.food_items.append(food_item)        
        print(" HURRAY! You Have Successfully Added the Food Item!")




    #defining function for editing the food
    def editing_food_items(self, food_id, name, quantity, price, discount, stock):
        for item in self.food_items:
            if item.food_id == food_id:
                item.name = name
                item.quantity = quantity
                item.price = price
                item.discount = discount
                item.stock = stock
                
                print("Hurray! You Have Successfully Edited Food Items")
                return
        print("The Food ID you enter is invalid or Does not Match")

    

    #defining the function to display the details of food items
    def view_food_items (self):
        #chceking if "self.food_items = []" is empty using 'len'
        if len(self.food_items) == 0:
            print("The Food Item Is Empty")
        else:
            for item in self.food_items:
                print("Food ID: {}".format(item.food_id))
                print("Food Name: {}".format(item.food_id))
                print("Food Quantity: {}".format(item.food_id))
                print("Food Price: {}".format(item.food_id))
                print("Food Discount: {}".format(item.food_id))
                print("Food Stock: {}".format(item.food_id))

    #defining the function to remove the food items
    def remove_food_items(self, food_id):
        for item in self.food_items:
            if item.food_id == food_id:
                self.food_items.remove(item)
                print("Hurray! You have Successfully Removed the Food Items")
                return
        print("The Food ID you enter is invalid or Does not Match")      




#Creating class for "User"
class User:
    def __init__(self,full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.order_history = []


    #function for placing_new_order
    def place_new_order (self, menu):
        print ("Here is Our Menu")
        for index, item in enumerate(menu, start= 1):  #here "start=1" representing, parameter is set to 1 and index starts from 1 
#using 'enumerate()" to iterate over the menu list obtain both index and corresponding item in each iteration

            #using f-string format
            print(f"{index}.{item.name} ({item.quantity}) [INR {item.price}]")
        
        items_selecting = input("Plesae Enter The Number of Item You want to Order (seperated by commas): ")
        items_selecting = [int(i) for i in items_selecting.split(",")]
        
        #creating the new list "order_items" by retrieving corresponding menu items from the selected items numbers
        order_items = [menu[i-1] for i in items_selecting]
        print("Items Are Selected!")


        for i in order_items:
            print(f"{i.name} ({i.quantity}) [INR {i.price}]")
        placing_order = input("Do you want to place an order from the selected items? Options:- Yes or No: ")
        if placing_order.lower() == "yes":
            
            #this line will generate the order id 
            order_id = random.randint(10000, 99999)

            order = {"order_id" : order_id, "items": order_items}   #this line will store Order ID and list of selected items
            self.order_history.append(order)
            print("Hurray! You Have Successfully Place an Order. Please wait for Max 20 Mins our Service Person Will Be Arriving to you With Delicious Foods. Thank You! ")



    #function for order History
    def view_order_history(self):
        if len(self.order_history) == 0:  #checking for the order history
            print("No order history available.")
        else:
            for order in self.order_history:
                print(f"Order ID: {order['order_id']}")   #retrieving all the order id
                print("Items:")
                for item in order['items']:
                    print(f"{item.name} ({item.quantity}) [INR {item.price}]")   #in this nested loop it prints order history items with name, quantity, and price



    #function for updating the profile 
    def update_profile(self):
        self.full_name = input("Enter your full name: ")
        self.phone_number = input("Enter your phone number: ")
        self.email = input("Enter your email: ")
        self.address = input("Enter your address: ")
        self.password = input("Enter your password: ")

        print("Hurray! You have successfully updated your profile.")


#defining the main function 
def main():
    admin = Admin()
    user = None     #keeping it none indicating there is no user logged in 
    menu = [
        FOODITEM ("Tandoori Chicken", "(4 pieces)",  "[INR 240]", "20%", "30"),
        FOODITEM ("Vegan Burger", "(1 Piece)", "[INR 320]", "30%", "10"),
        FOODITEM ("Truffle Cake", "(500gm)", "[INR 900]", "25%", "15"),
    ]


    while True:
        print("1. Admin Login")
        print("2. User Login")
        print("3. Exit")
        choice = int(input("Please choose the number from the above mentioned!: "))

        if choice == 1:
            admin_username = input("Enter your username: ")
            admin_password = input("Enter your password: ")


            # perform admin authentication
            if admin_username == "admin" and admin_password == "admin123":


                while True :
                    print ("This page is only for Admin! If you're not admin, kindly exit!")
                    print("1. Add new food item")
                    print("2. Edit food item")
                    print("3. View food items")
                    print("4. Remove food item")
                    print("5. Logout")  
                    admin_choice = int(input("Admin, please enter your choice: "))                  


                    if admin_choice == 1:
                        name = input("Enter food item name: ")
                        quantity = input("Enter food item quantity: ")
                        price = float(input("Enter food item price: "))
                        discount = float(input("Enter food item discount: "))
                        stock = int(input("Enter food item stock: "))
                        admin.add_food_item(name, quantity, price, discount, stock)
          
          
                    elif admin_choice == 2:
                        food_id = int(input("Enter food item ID to edit: "))
                        name = input("Enter food item name: ")
                        quantity = input("Enter food item quantity: ")
                        price = float(input("Enter food item price: "))
                        discount = float(input("Enter food item discount: "))
                        stock = int(input("Enter food item stock: "))
                        admin.edit_food_item(food_id, name, quantity, price, discount, stock)
                    
                    elif admin_choice == 3:
                        admin.view_food_items()
                    
                    elif admin_choice == 4:
                        food_id = int(input("Enter food item ID to remove: "))
                        admin.remove_food_item(food_id)
                    
                    elif admin_choice == 5:
                        break
                    
                    else:
                        print("Admin, you enter invalid choice! Please try again.")
            else:
                print("Invalid admin credentials!")

        
        
        elif choice == 2:

            #if user is first time user , create the profile
            if user is None:
                full_name = input("Please enter your full name: ")
                phone_number = input("Please enter your phone number: ")
                email = input("Please enter your email: ")
                address = input("Please enter your address: ")
                password = input("Please enter your password: ")
                user = User(full_name, phone_number, email, address, password)
                print("You are signed in")
            
            #if user already has a profile or account
            else:
                login_email = input("Enter your email: ")
                login_password = input("Enter your password: ")



                # Perform user authentication
                if login_email == user.email and login_password == user.password:
                    while True:
                        print("This Page is Only for User! ")
                        print("1. Place New Order")
                        print("2. Order History")
                        print("3. Update Profile")
                        print("4. Logout")
                        user_choice = int(input("Please enter your choice: "))


                        if user_choice == 1:
                            user.place_new_order(menu)

                        elif user_choice == 2:
                            user.view_order_history()

                        elif user_choice == 3:
                            user.update_profile()

                        elif user_choice == 4:
                            user = None
                            break

                        else:
                            print("You enter invalid choice! Please try again.")
                
                else:
                    print("Invalid user credentials!")

        elif choice == 3:
            print("Thank you for coming to KONYAK's Restaurant!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()











