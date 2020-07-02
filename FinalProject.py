# 1673728
# Zheng

import csv

product_list = []


class Product(object):
    def __init__(self, item_ID, manufacturer_name, item_type, is_damaged, item_price, service_date):
        self.item_ID = item_ID
        self.manufacturer_name = manufacturer_name
        self.item_type = item_type
        self.is_damaged = is_damaged
        self.item_price = item_price
        self.service_date = service_date


def get_manufacturer(Product):
    return Product.manufacturer_name


with open('ManufacturerList.csv') as file:
    reader = csv.reader(file, delimiter=",")
    for row in reader:
        item_ID = row[0]
        manufacturer_name = row[1]
        item_type = row[2]
        is_damaged = row[3]
        product = Product(item_ID, manufacturer_name, item_type, is_damaged, None, None)
        product_list.append(product)

with open('PriceList.csv') as file:
    reader = csv.reader(file, delimiter=",")
    for row in reader:
        item_ID = row[0]
        item_price = row[1]
        for product in product_list:
            if product.item_ID == item_ID:
                product.item_price = item_price

with open('ServiceDatesList.csv') as file:
    reader = csv.reader(file, delimiter=",")
    for row in reader:
        item_ID = row[0]
        service_date = row[1]
        for product in product_list:
            if product.item_ID == item_ID:
                product.service_date = service_date

full_inventory = product_list
full_inventory.sort(key=get_manufacturer)
with open('FullInventory.csv', 'w') as file:
    for row in full_inventory:
        item_ID = row.item_ID
        manufacturer_name = row.manufacturer_name
        item_type = row.item_type
        item_price = row.item_price
        service_date = row.service_date
        is_damaged = row.is_damaged
        string = item_ID + ',' + manufacturer_name + ',' + item_type + ',' + item_price + ',' + service_date + ',' + is_damaged + '\n'
        file.write(string)

item_types = []
for product in product_list:
    is_found = False
    for item_type in item_types:
        if item_type == product.item_type:
            is_found = True
    if not is_found:
        item_types.append(product.item_type)
for item_type in item_types:
    with open(item_type + ".csv", 'w') as file:
        for product in product_list:
            if item_type == product.item_type:
                item_ID = product.item_ID
                manufacturer_name = product.manufacturer_name
                item_price = product.item_price
                service_date = product.service_date
                is_damaged = product.is_damaged
                string = item_ID + ',' + manufacturer_name + ',' + item_price + ',' + service_date + ',' + is_damaged + '\n'
                file.write(string)

damaged_inventory = []
for product in product_list:
    damaged_is = False
    for is_damaged in damaged_inventory:
        if is_damaged == product.is_damaged:
            damaged_is = True
        if not damaged_is:
            damaged_inventory.append(product.is_damaged)
for is_damaged in damaged_inventory:
    with open('DamagedInventory.csv', 'w') as file:
        for product in product_list:
            if is_damaged == product.is_damaged:
                item_ID = product.item_ID
                manufacturer_name = product.manufacturer_name
                item_type = product.item_type
                item_price = product.item_price
                service_date = product.service_date
                is_damaged = product.is_damaged
                string = item_ID + ',' + manufacturer_name + ',' + item_type + ',' + item_price + ',' + service_date + ',' + is_damaged + '\n'
                file.write(string)

if __name__ == "__main__":
    manufacturer = ''
    type_item = ''
    while manufacturer != 'q' and type_item != 'q':
        manufacturer = input('Input manufacturer name: \n')
        type_item = input('Input item type: \n')
        for product in product_list:
            if product.manufacturer_name == manufacturer and product.item_type == type_item:
                item_ID = product.item_ID
                manufacturer_name = product.manufacturer_name
                item_type = product.item_type
                item_price = product.item_price
                string = item_ID + ',' + manufacturer_name + ',' + item_price + ',' + service_date
                print(f"Your item is {string}")
            else:
                print('No such item in inventory')





