"""

Abhimanyu Kidarithil Meethal
PSID: 2105385

"""
import csv
import datetime

def read_file(file_name):
    data = []
    with open(file_name, 'r') as file:
        reader = file.readlines()
        for row in reader:
            data.append(row)
    return data

def write_csv(filename, data, fieldnames):
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        cleaned_data = []
        for i in data:
            item_data = {key: i[key] for key in fieldnames}
            cleaned_data.append(item_data)
        writer.writerows(cleaned_data)

def merge_data(manufacturer_list, price_list, service_dates_list):
    inventory = []
    for item in manufacturer_list:
        item = item.split(",")
        item_id = item[0]
        manufacturer_name = item[1]
        item_type = item[2]
        damaged = item[3].strip()

        price = find_price(item_id, price_list)
        service_date = find_service_date(item_id, service_dates_list)

        inventory.append({
            'Item ID': item_id,
            'Manufacturer Name': manufacturer_name,
            'Item Type': item_type,
            'Price': price,
            'Service Date': service_date,
            'Condition': damaged
        })

    return inventory

def find_price(item_id, price_list):
    for p in price_list:
        p = p.split(",")
        if item_id == p[0]:
            price = p[1].strip()
            return price
    return ''

def find_service_date(item_id, service_dates_list):
    for s in service_dates_list:
        s = s.split(",")
        if item_id == s[0]:
            service_date = s[1].strip()
            return service_date
    return ''

def sort_inventory_by_manufacturer(inventory):
    inventory.sort(key=get_manufacturer_name)

def get_manufacturer_name(item):
    return item['Manufacturer Name']

def sort_inventory_by_service_date(inventory):
    for item in inventory:
        item['Service Date'] = datetime.datetime.strptime(item['Service Date'], '%m/%d/%Y')

    inventory.sort(key=get_service_date)

    for item in inventory:
        item['Service Date'] = item['Service Date'].strftime('%m/%d/%Y')

def get_service_date(item):
    return item['Service Date']
def sort_inventory_by_price_descending(inventory):
    inventory.sort(key=get_price_descending)
def get_price_descending(item):
    return -float(item['Price'])
def convert_to_datetime(date_str):
    return datetime.datetime.strptime(date_str, '%m/%d/%Y').date()
def sort_items_by_item_id(item):
    return item['Item ID']

# Reading
manufacturer_list = read_file('ManufacturerList.csv')
price_list = read_file('PriceList.csv')
service_dates_list = read_file('ServiceDatesList.csv')

# Merging
inventory = merge_data(manufacturer_list, price_list, service_dates_list)

# Sorting by Manufacturer Name
sort_inventory_by_manufacturer(inventory)

# Generating FullInventory.csv
write_csv('FullInventory.csv', inventory,
          ['Item ID', 'Manufacturer Name', 'Item Type', 'Price', 'Service Date', 'Condition'])

# Generating Item-type specific inventory files
item_types = list(set([item['Item Type'] for item in inventory]))
for item_type in item_types:
    items_of_type = [item for item in inventory if item['Item Type'] == item_type]
    items_of_type.sort(key=sort_items_by_item_id)
    item_type_filename = f'{item_type.capitalize()}Inventory.csv'
    write_csv(item_type_filename, items_of_type, ['Item ID', 'Manufacturer Name', 'Price', 'Service Date', 'Condition'])


# Generating PastServiceDateInventory.csv
for item in inventory:
    item['Service Date'] = convert_to_datetime(item['Service Date'])

past_service_date_inventory = [item for item in inventory if item['Service Date'] < datetime.datetime.now().date()]
past_service_date_inventory.sort(key=get_service_date)

for item in past_service_date_inventory:
    item['Service Date'] = item['Service Date'].strftime('%m/%d/%Y')

write_csv('PastServiceDateInventory.csv', past_service_date_inventory,
          ['Item ID', 'Manufacturer Name', 'Item Type', 'Price', 'Service Date', 'Condition'])


# Generating DamagedInventory.csv
sort_inventory_by_price_descending(inventory)
damaged_inventory = [item for item in inventory if item['Condition'].lower() == 'damaged']
write_csv('DamagedInventory.csv', damaged_inventory,
          ['Item ID', 'Manufacturer Name', 'Item Type', 'Price', 'Service Date'])
