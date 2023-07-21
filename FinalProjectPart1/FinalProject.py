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
        cleaned_data = [{key: i[key] for key in fieldnames} for i in data]
        writer.writerows(cleaned_data)
# Reading
manufacturer_list = read_file('ManufacturerList.csv')
price_list = read_file('PriceList.csv')
service_dates_list = read_file('ServiceDatesList.csv')

# Merging
inventory = []
price = ""
service_date = ""
for item in manufacturer_list:
    item = item.split(",")
    item_id = item[0]
    manufacturer_name = item[1]
    item_type = item[2]
    item[3] = item[3].strip()
    damaged = item[3]

    for p in price_list:
        p = p.split(",")
        if item_id == p[0]:
            price = p[1]
            price = price.strip()
    for s in service_dates_list:
        s = s.split(",")
        if item_id == s[0]:
            service_date = s[1]
            service_date = service_date.strip()

    inventory.append({
        'Item ID': item_id,
        'Manufacturer Name': manufacturer_name,
        'Item Type': item_type,
        'Price': price,
        'Service Date': service_date,
        'Condition': damaged
    })

# Sorting
inventory.sort(key=lambda x: x['Manufacturer Name'])

# Generating FullInventory.csv
write_csv('FullInventory.csv', inventory,
          ['Item ID', 'Manufacturer Name', 'Item Type', 'Price', 'Service Date', 'Condition'])

# Generating Item-type specific inventory files
item_types = list(set([item['Item Type'] for item in inventory]))
for item_type in item_types:
    items_of_type = [item for item in inventory if item['Item Type'] == item_type]
    items_of_type.sort(key=lambda x: x['Item ID'])
    item_type_filename = f'{item_type.capitalize()}Inventory.csv'
    write_csv(item_type_filename, items_of_type, ['Item ID', 'Manufacturer Name', 'Price', 'Service Date', 'Condition'])

# Generating PastServiceDateInventory.csv
# Parsing the service dates in the inventory to datetime objects
for item in inventory:
    item['Service Date'] = datetime.datetime.strptime(item['Service Date'], '%m/%d/%Y')

past_service_date_inventory = [item for item in inventory if item['Service Date'] < datetime.datetime.now()]
past_service_date_inventory.sort(key=lambda x: x['Service Date'])

# Convert the service dates back to strings in the MM/DD/YYYY format for CSV writing
for item in past_service_date_inventory:
    item['Service Date'] = item['Service Date'].strftime('%m/%d/%Y')

write_csv('PastServiceDateInventory.csv', past_service_date_inventory,
          ['Item ID', 'Manufacturer Name', 'Item Type', 'Price', 'Service Date', 'Condition'])

# Generating DamagedInventory.csv
damaged_inventory = [item for item in inventory if item['Condition'].lower() == 'damaged']
damaged_inventory.sort(key=lambda x: float(x['Price']), reverse=True)
for item in damaged_inventory:
    item['Service Date'] = item['Service Date'].strftime('%m/%d/%Y')
write_csv('DamagedInventory.csv', damaged_inventory,
          ['Item ID', 'Manufacturer Name', 'Item Type', 'Price', 'Service Date'])
