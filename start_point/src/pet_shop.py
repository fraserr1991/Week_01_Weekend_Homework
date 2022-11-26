
def get_pet_shop_name(pet_shop_name):
    find_pet_shop_name = pet_shop_name["name"] 

    return find_pet_shop_name

def get_total_cash(pet_shop_total_cash):
    find_pet_shop_total_cash = pet_shop_total_cash["admin"]["total_cash"]

    return find_pet_shop_total_cash

def add_or_remove_cash(pet_shop, cash_added_or_removed):
    pet_shop["admin"]["total_cash"] += cash_added_or_removed

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop,sold_pets):
    pet_shop["admin"]["pets_sold"] += sold_pets

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    breed_type_list = []

    for breed_type in pet_shop["pets"]:
        if breed_type["breed"] == breed:
            # breed_type_list += [breed_type["breed"]] #this works but I think append is probably nicer
            breed_type_list.append(breed_type["breed"])

    return breed_type_list
    # total_breed = 0
    # for breed_type in pet_shop["pets"]:
    #     if breed_type["breed"] == breed:
    #         total_breed += 1
            
    # return total_breed, len(pet_shop["pets"])

def find_pet_by_name(pet_shop, a_pet_name):
    for pet_name in pet_shop["pets"]:
        if pet_name["name"] == a_pet_name:
            return pet_name
    return None

def remove_pet_by_name(pet_shop, a_pet_name):
    for pet_name in pet_shop["pets"]:
        if pet_name["name"] == a_pet_name:
            pet_shop["pets"].remove(pet_name)
    return None  

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer_number_1):
    return customer_number_1["cash"]

        # for customer in customer_number_1["customers"]:
        #     if customer == [0]:
        #         return customer["cash"]

def remove_customer_cash(customer_number_1, cash):
    customer_number_1["cash"] += (-cash)
    return customer_number_1["cash"]

def get_customer_pet_count(customer_number_1):
    total_pets = 0
    
    for pet in customer_number_1["pets"]:
        total_pets += 1
    return total_pets

def add_pet_to_customer(customer_number_1, new_pet):
    customer_number_1["pets"] = [new_pet]

def customer_can_afford_pet(customer, pet_cost):
        if customer["cash"] >= pet_cost["price"]:
            return True
        else:
            return False

def sell_pet_to_customer(pet_shop, pet, customer):
        
        if pet == None:
            return False
        
        if customer["cash"] >= pet["price"]:
            customer["cash"] += (-pet["price"])
            customer["pets"].append(pet["name"])
            pet_shop["admin"]["pets_sold"] += 1
            pet_shop["admin"]["total_cash"] += pet["price"]
        else:
            print("Insufficent funds")
            return False