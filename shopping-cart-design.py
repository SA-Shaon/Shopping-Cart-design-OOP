"""
    Shopping Cart Design

    User ->Customer -->add item to the cart
         |           --> update cart
         |          --> delete cart
         |->Admin-->add product
                 --> update product
                 --> delete product
"""


class User:
    user_lst = []  # class variable . user database

    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password


class Item:
    def __init__(self, itemID, price, description, quantity) -> None:
        self.itemID = itemID
        self.pricr = price
        self.description = description
        self.quantity = quantity


class ShoppingBasket:
    user_lst = []
    # [{"name": "rahat", "password":"1234"},{"name": "shaon", "password":"1234"}]
    user_ordered_data = {}
    # {"rahat:[{"itemID":12,"price":200, "description":"abcd", "quantity":12},{"itemID":12,"price":200, "description":"abcd", "quantity":12}]"}
    itemDB = []
    # [{"itemID":itemID, "price":price, "description": description},{"itemID":itemID, "price":price, "description": description}]

    def get_userlst(self):
        return self.user_lst

    def create_account(self):
        name = input("Enter your username: ")
        isNameExist = False
        for user in self.get_userlst():
            if user.username == name:
                print("Account already created.")
                isNameExist = True
                break
        if not isNameExist:
            password = input("Enter your password: ")
            self.new_user = User(name, password)
            self.user_lst.append(vars(self.new_user))
            print("Account created.")

    def addItemToDatabase(self):
        itemID = input("Enter itemID: ")
        description = input("Enter item description: ")
        price = int(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))

        self.new_item = Item(itemID, description, price, quantity)
        self.itemDB.append(vars(self.new_item))

    def addItemToCart(self, username):
        itemID = input("Enter Item Id: ")
        quantity = int(input("Enter item Quantity: "))
        flag = 0
        for i in self.itemDB:
            if i['itemID'] == itemID and i['quantity'] >= quantity:
                print("Items available")
                flag = 1
                break
        if flag == 1:
            print("Iteams not available")
        else:
            self.user_ordered_data[username] = [
                {'itemID': itemID, 'quantity': quantity}]

    def updateProductCart(self, username):
        itemID = input("Enter item ID: ")
        quantity = int(input("Enter updated quantity Number: "))
        for i in self.user_ordered_data[username]:
            if i['itemID'] == itemID:
                if quantity <= i['quantity']:
                    i['quantity'] = quantity
                else:
                    print("Out of stock.")
                    break

    def deleteProductCart(self, username):
        itemID = input("Enter item ID you wnat to delete: ")
        flag = 0
        for i in self.itemDB:
            if i['itemID'] == itemID:
                print("Items available")
                flag = 1
                break
        if flag:
            for i in self.user_ordered_data[username]:
                if i['itemID'] == itemID:
                    self.user_ordered_data[username].remove(i)

    def showDB(self):
        print(self.itemDB)
        print(self.user_ordered_data)
        print(self.user_lst)


# b = ShoppingBasket()
# b.create_account()
# users = b.get_userlst()
# print(users)

basket = ShoppingBasket()
basket.addItemToDatabase()
basket.showDB()
while True:
    print("1. Create an Account.\n2. Login to Your Account. \n3.EXIT")
    user_choice = int(input("Enter your choice: "))
    if user_choice == 3:
        break
    elif user_choice == 1:
        basket.create_account()
    elif user_choice == 2:
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        isNameExist = False
        for user in basket.user_lst:
            if user['username'] == name and user['password'] == password:
                isNameExist = True
                break
        if isNameExist:
            while True:
                print(
                    "1.Add item to your cart\n 2.Update your cart \n3. Delete your cart\n 4.Show your cart \n5.EXIT")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    basket.addItemToCart(name)
                elif choice == 2:
                    basket.updateProductCart(name)
                elif choice == 3:
                    basket.deleteProductCart(name)
                elif choice == 4:
                    basket.showDB()
                else:
                    break
        else:
            print("You have no account.")
