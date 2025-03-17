from pathlib import Path

# 1) There is such a file... your task is to write only emails with the gmail.com domain to a new file (the hash on the left does not need to be written)

directory_path = Path.cwd()
additional_files = directory_path.joinpath('additional_files')
try:
    with (open(additional_files.joinpath('emails.txt'), 'r') as file,
          open(additional_files.joinpath('new_file.txt'), 'w') as new_file):
        for line in [row.split() for row in file.readlines()]:
            for word in line:
                if word.find('@gmail.com') != -1:
                    new_file.write(word + '\n')

except Exception as e:
    print(e)


# 2) Create a shopping notebook:
# - the purchase must have an id, name and price+
# - we save all purchases in a file+
# from the functionality:
# * output of all purchases+
# * it should be possible to add a purchase to the book +
# * it should be possible to search for a purchase by any field +
# * it should be possible to show the most expensive purchase +
# * it should be possible to delete a purchase by id
# (well, that's all the menu is for)

class Purchase:
    directory_path = Path.cwd()
    additional_files = directory_path.joinpath('additional_files')

    def __init__(self, id_purchase=None, name=None, price=None):
        self.id_purchase = id_purchase
        self.name = name
        self.price = price

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()

    def __call__(self, id_purchase, name, price):
        self.id_purchase = id_purchase
        self.name = name
        self.price = price

    def show_purchase_list(self):
        if self.additional_files.joinpath('purchase_list.txt').exists():
            with open(additional_files.joinpath('purchase_list.txt'), 'r') as file_purchase_list:
                return file_purchase_list.read()
        with open(additional_files.joinpath('purchase_list.txt'), 'w') as file_purchase_list:
            return file_purchase_list.write('Purchase list:')

    def add(self, instance: 'Purchase') -> None:
        with open(self.additional_files.joinpath('purchase_list.txt'), 'a') as file_purchase_list:
            file_purchase_list.write(f"id: {instance.id_purchase}, name: {instance.name}, price: {instance.price} \n")

    def search(self, search_params: str):
        try:
            with open(self.additional_files.joinpath('purchase_list.txt'), 'r') as file_purchase_list:
                found = False
                for row in file_purchase_list.readlines():
                    if row.find(search_params) != -1:
                        print(row.strip())
                        found = True
                if not found:
                    raise TypeError(f'nothing find for your request')

        except Exception as error:
            print(error)

    def purchase_with_higher_price(self):
        with open(self.additional_files.joinpath('purchase_list.txt'), 'r') as file_purchase_list:
            prices = []
            for lines in [row.split(',') for row in file_purchase_list.readlines()]:
                for row in [row.strip() for row in lines if row.find('price: ') != -1]:
                    prices.append(int(row.split(': ')[1]))

            if prices:
                max_prices = max(prices)
                print(f'max price of purchase {max_prices}')

    def delete(self, id_purchase: str):
        try:
            with open(self.additional_files.joinpath('purchase_list.txt'), 'r') as file_purchase_list:
                lines = file_purchase_list.readlines()
                found = False
            with open(self.additional_files.joinpath('purchase_list.txt'), 'w') as temp_purchase_list:
                for row in lines:
                    if f"id: {id_purchase}" in row:
                        found = True
                        print(f"Purchase with ID {id_purchase} removed.")
                    else:
                        temp_purchase_list.write(row)

            if not found:
                print(f"ID {id_purchase} not found.")

        except Exception as error:
            print(f"Error: {error}")


purchase = Purchase()

banana = Purchase(2, 'banana', 200)
cherry = Purchase(5, 'cherry', 500)
strawberry = Purchase(25, 'strawberry', 300)

# purchase.add(banana)
# purchase.add(cherry)
# purchase.add(strawberry)
# print(purchase.show_purchase_list())
# purchase.search('ban3')
# purchase.purchase_with_higher_price()
purchase.delete('5')
