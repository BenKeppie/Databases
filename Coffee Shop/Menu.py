from create_product_table import *
from delete_existing_product import *
from insert_product_data import *
from select_existing_products import *
from update_product_data import *



def display_menu():
    print()
    print("Product Table Management")
    print()
    print("1. (Re)Create Product Table")
    print("2. Add new product")
    print("3. Edit existing product")
    print("4. Delete existing product")
    print("5. Search for products")
    print("0. Exit")

def get_menu_option():
    Option=int(input("Please select an option: "))
    return Option

def create_product_table():
    db_name="coffee_shop.db"
    sql= """create table Product (ProductID integer, Name text, Price real, Primary Key(ProductID))"""
    create_table(db_name,"Product", sql)
    print("Blank Product Table Created.")

def add_new_product():
    pass

def edit_existing_product():
    pass

def delete_existing_product():
    pass

def search_for_product():
    pass



if __name__ =="__main__":
    Finished=False
    while not Finished:
        display_menu()
        Choice=get_menu_option()
        if Choice==0:
            Finished=True
            print()
        else:
            print()
    print("Menu Terminated")
