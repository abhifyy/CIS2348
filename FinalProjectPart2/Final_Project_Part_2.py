"""

Abhimanyu Kidarithil Meethal
PSID: 2105385

"""
import datetime


def find_closest_price_item(similar_items, most_expensive_item):
    def get_item_price_difference(item):
        return abs(float(item['Price']) - float(most_expensive_item['Price']))

    closest_price_item = min(similar_items, key=get_item_price_difference)
    return closest_price_item


def find_most_expensive_item(items):
    def get_item_price(item):
        return float(item['Price'])

    most_expensive_item = max(items, key=get_item_price)
    return most_expensive_item


class InventoryManager:
    def _init_(self):
        self.inventory = []

    @staticmethod
    def read_file(file_name):
        data = []
        with open(file_name, 'r') as file:
            reader = file.readlines()
            for row in reader:
                data.append(row)
        return data

        def merge_data(self, manufacturer_list, price_list, service_dates_list):
            for item in manufacturer_list:
                item = item.split(",")
                item_id = item[0]
                manufacturer_name = item[1]
                item_type = item[2]
                damaged = item[3].strip()

                price = self.find_price(item_id, price_list)
                service_date = self.find_service_date(item_id, service_dates_list)
                service_date = datetime.datetime.strptime(service_date, '%m/%d/%Y')

                self.inventory.append({
                    'Item ID': item_id,
                    'Manufacturer Name': manufacturer_name,
                    'Item Type': item_type,
                    'Price': price,
                    'Service Date': service_date,  # Now it's a datetime object
                    'Condition': damaged
                })
    def find_price(self, item_id, price_list):
        for p in price_list:
            p = p.split(",")
            if item_id == p[0]:
                price = p[1].strip()
                return price
        return ''

    def find_service_date(self, item_id, service_dates_list):
        for s in service_dates_list:
            s = s.split(",")
            if item_id == s[0]:
                service_date = s[1].strip()
                return service_date
        return ''

    def sort_inventory_by_manufacturer(self):
        self.inventory.sort(key=self.get_manufacturer_name)

    def get_manufacturer_name(self, item):
        return item['Manufacturer Name']

    def merge_data(self, manufacturer_list, price_list, service_dates_list):
        self.inventory = []
        for item in manufacturer_list:
            item = item.split(",")
            item_id = item[0]
            manufacturer_name = item[1]
            item_type = item[2]
            damaged = item[3].strip()

            price = self.find_price(item_id, price_list)
            service_date = self.find_service_date(item_id, service_dates_list)

            # Convert 'Service Date' to datetime object
            service_date = datetime.datetime.strptime(service_date, '%m/%d/%Y')

            self.inventory.append({
                'Item ID': item_id,
                'Manufacturer Name': manufacturer_name,
                'Item Type': item_type,
                'Price': price,
                'Service Date': service_date,  # Now it's a datetime object
                'Condition': damaged
            })

    def query_inventory(self, input_query):
        self.manufacturer = ""  # Reset manufacturer before querying
        self.item_type = ""  # Rese item_type before querying
        input_query = input_query.strip(",")
        words = input_query.split()

        for word in words:
            for item in self.inventory:
                if self.manufacturer == "" or item['Manufacturer Name'].lower() == word:
                    self.manufacturer = item['Manufacturer Name'].lower()
                if self.item_type == "" and item['Item Type'].lower() == word:
                    self.item_type = item['Item Type'].lower()

        if not self.manufacturer or not self.item_type:
            return

        matched_items = [item for item in self.inventory if item['Manufacturer Name'].lower() == self.manufacturer and
                         item['Item Type'].lower() == self.item_type and
                         item['Service Date'] >= datetime.datetime.now() and
                         item['Condition'].lower() != 'damaged']
        if not matched_items:
            return

        return matched_items

    def output(self, matched_items):
        if matched_items == None:
            print("No item from this manufacturer and type is available.")
            return
        if matched_items == 0:
            print("No item from this manufacturer and type is available.")
            return

        # Find the most expensive item
        self.most_expensive_item = find_most_expensive_item(matched_items)

        print("Your item is:")
        print(
            f"Item ID: {self.most_expensive_item['Item ID']}, Manufacturer: "
            f"{self.most_expensive_item['Manufacturer Name']}, Item Type: {self.most_expensive_item['Item Type']}"
            f", Price: {self.most_expensive_item['Price']}")

    def similar(self):
        # Find similar item from another manufacturer
        similar_items = [item for item in self.inventory if item['Manufacturer Name'].lower() != self.manufacturer and
                         item['Item Type'].lower() == self.item_type and
                         item['Service Date'] >= datetime.datetime.now() and
                         item['Condition'].lower() != 'damaged']

        if len(similar_items) > 0:
            closest_price_item = find_closest_price_item(similar_items, self.most_expensive_item)
            print("You may also consider:")
            print(
                f"Item ID: {closest_price_item['Item ID']}, Manufacturer: {closest_price_item['Manufacturer Name']}"
                f", Item Type: {closest_price_item['Item Type']}, Price: {closest_price_item['Price']}")

        else:
            print("No similar item from another manufacturer available.")

# Reading data from CSV files
manager = InventoryManager()
manufacturer_list = manager.read_file('ManufacturerList.csv')
price_list = manager.read_file('PriceList.csv')
service_dates_list = manager.read_file('ServiceDatesList.csv')

manager.merge_data(manufacturer_list, price_list, service_dates_list)
manager.sort_inventory_by_manufacturer()
i = 0
while i != 1:
    inp = input("Enter the manufacturer and item type else enter q to quit: ").strip().lower()

    if inp == "q":
        i = 1
    if i == 0:
        matched_items = manager.query_inventory(inp)

        manager.output(matched_items)
        manager.similar()
