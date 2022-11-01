from abc import ABC, abstractmethod

# how to create an object from a class 
# object_name =className(arg)
# but abstract classes cant be instantiated

class User:
    first_name = ""
    last_name = ""
    email = ""
    alias = ""
    password = ""
    id = ""

class UserAbstract(ABC):
    @abstractmethod
    def create_user(self, ):
        pass 

    @abstractmethod
    def get_all_users(self):
        pass
    @abstractmethod
    def get_user_by_id(self, user_id):
        pass

class UserManager(UserAbstract):
        def create_user(self, user:User):
            print('user information')
        
        def get_all_users(self):
            print("hello tiny! we are getting all users here")
        
        def get_user_by_id(self, user_id):
            first_name = "Olamide"
            last_name = "Ahmed"
            print(f"hello world {first_name} {last_name} {user_id}")
class Product:
    product_type = ""
    product_name = ""
    product_weight = ""
    product_quantity = ""
    product_size = ""
    product_color = ""

class ProductAbstract(ABC):

    @abstractmethod
    def Select_product(self):
        pass

    @abstractmethod
    def Add_to_cart(self):
        pass

    @abstractmethod
    def Select_color(self,):
        pass

class ProductManager(ProductAbstract):
        def Select_product(self, product_name):
            print(f"Your selected products are {product_name}")
        def Add_to_cart(self, product_quantity):
            print(f"{product_quantity} quantity have been added to your cart")
        def Select_color(self, product_color):
            print(f"Product color is {product_color}")

user_manager = UserManager()
user_manager.get_all_users()
user_manager.get_user_by_id(78)


product_manager = ProductManager()
product_manager.Select_product("Omo detergent")
product_manager.Select_color("Blue")
product_manager.Add_to_cart(5)