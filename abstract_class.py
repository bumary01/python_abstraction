from abc import ABC, abstractmethod
class Product:
    product_type = ""
    product_name = ""
    product_weight = ""
    product_quantity = ""
    product_size = ""
    product_color = ""
    product_id = 0
    product_image = ""

class ProductAbstract(ABC):

    @abstractmethod
    def Create_product(self):
        pass
    @abstractmethod
    def Edit_product(self):
        pass
    @abstractmethod
    def Get_product_by_id(self):
        pass
    @abstractmethod
    def Get_all_products(self):
        pass
    @abstractmethod
    def Upload_product_image(self):
        pass
    @abstractmethod
    def Delete_product(self):
        pass


class ProductManager(ProductAbstract):
        def Create_product(self, product_name):
            print(f"Your products are {product_name}")

        def Edit_product(self, product_quantity):
            print(f"{product_quantity} quantity have been added to your cart")

        def Get_product_by_id(self, product_id):
            print(f"Product id is {product_id}")

        def Get_all_products(self):
            print(f"These are all your products")

        def Upload_product_image(self, product_image):
            print(f"product image {product_image}")

        def Delete_product(self,):
            print(f"product deleted")




product_manager = ProductManager()
product_manager.Create_product("Omo detergent")
product_manager.Edit_product("Blue")
product_manager.Get_product_by_id(5)
product_manager.Get_all_products()
product_manager.Upload_product_image("")
product_manager.Delete_product()
