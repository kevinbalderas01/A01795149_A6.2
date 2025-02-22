'''
sys -> To get parameters from terminal
os -> To manage files, creation and deletion
time -> To manage start and end time to measure execution
json -> To manage json files and getting content in the form of a dict
'''
# pylint: disable=invalid-name
import sys
import os
import time
import json


class Hotels:
    '''
    Class that implements a hotel based on attributes
    '''
    def __init__(self):
        self.hotels = []
        self.counter = 0
        self.hotels_filename = 'Hotels.json'
        self.hotel_name = ''
        self.hotel_address = ''
        self.hotel_phone_number = ''
        self.hotel_rooms = 0

    def generate_id(self):
        '''
        Method that generates an id
        '''
        self.counter += 1
        return self.counter

    def create_all_hotels(self, file_name):
        '''
        Method that created a bunch of new hotels
        '''
        temp_hotels = read_from_json(file_name)
        for hotel in temp_hotels:
            try:
                name = hotel["name"]
                address = hotel["address"]
                phone_number = hotel["phone_number"]
                rooms = hotel["rooms"]
                new_hotel = self.create_hotel(
                    name, address, phone_number, rooms)
                self.hotels.append(new_hotel)
            except (FileNotFoundError, IndexError) as error:
                print('Wrong field, You need, id, hotel name,\
                      address, phone number and rooms', error)
        write_to_json(self.hotels, 'Hotels.json')
        self.display_hotel_info()
        return temp_hotels

    def create_hotel(self, name, address, phone_number, rooms):
        '''
        Method that creates a new hotel based on attributes
        '''
        self.hotel_name = name
        self.hotel_address = address
        self.hotel_phone_number = phone_number
        self.hotel_rooms = rooms

        id_hotel = self.generate_id()
        hotel_obj = {'id': id_hotel, 'hotel_name': self.hotel_name,
                     'hotel_address': self.hotel_address,
                     'hotel_phone_number': self.hotel_phone_number,
                     'hotel_rooms': self.hotel_rooms}
        return hotel_obj

    def display_hotel_info(self):
        '''
        Method that displays hotel information, updated information
        '''
        db = read_from_json(self.hotels_filename)
        for hotel in db:
            print(hotel)
        return True

    def modify_hotel_info(self, filename):
        '''
        Method that modify or updates information only on certain records
        '''
        hotels_to_update = read_from_json(filename)
        db = read_from_json(self.hotels_filename)
        for hotel in db:
            for h_update in hotels_to_update:
                # Just update necesarry items, not all of them
                if hotel['id'] == h_update['id']:
                    hotel['id'] = h_update['id']
                    hotel['hotel_name'] = h_update['name']
                    hotel['hotel_address'] = h_update['address']
                    hotel['hotel_phone_number'] = h_update['phone_number']
                    hotel['hotel_rooms'] = h_update['rooms']

        self.hotels = db
        write_to_json(self.hotels, 'Hotels.json')
        self.display_hotel_info()
        return db


class Customers:
    '''
    Class that implements customers based on attributes
    '''
    def __init__(self):
        self.customers = []
        self.counter = 0
        self.customer_filename = 'Customers.json'
        self.first_name = ''
        self.last_name = ''
        self.phone_number = ''

    def generate_id(self):
        '''
        Method that generates an id
        '''
        self.counter += 1
        return self.counter

    def create(self, file_name):
        '''
        Method that created a bunch of new customerss
        '''
        temp_customers = read_from_json(file_name)
        for customer in temp_customers:
            try:
                first_name = customer["first_name"]
                last_name = customer["last_name"]
                phone_number = customer["phone_number"]
                new_customer = self.create_customer(
                    first_name, last_name, phone_number)
                self.customers.append(new_customer)
            except (FileNotFoundError, IndexError) as error:
                print('Wrong field, You need, id, first name,\
                      last name and phone number', error)
        write_to_json(self.customers)
        self.display_customer_info()
        return temp_customers

    def create_customer(self, first_name, last_name, phone_number):
        '''
        Method that creates a new client based on attributes
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        id_customer = self.generate_id()
        customer_obj = {'id': id_customer, 'first_name': self.first_name,
                        'last_name': self.last_name,
                        'phone_number': self.phone_number}
        return customer_obj

    def delete_customer(self, filename):
        '''
        Method that deletes customers based on info from file
        '''
        new_customers = []
        new_keys = []
        customers = read_from_json(filename)
        customers_to_delete = [i['id'] for i in customers]
        db = read_from_json(self.customer_filename)
        customers_db = [i['id'] for i in db]
        db = read_from_json(self.customer_filename)

        for k1 in customers_db:
            if k1 not in customers_to_delete:
                new_keys.append(k1)
        for customer in db:
            if customer['id'] in new_keys:
                new_customers.append(customer)
        self.customers = new_customers
        write_to_json(self.customers)
        self.display_customer_info()
        return new_customers

    def display_customer_info(self):
        '''
        Method that displays customer information, updated information
        '''
        db = read_from_json(self.customer_filename)
        for customer in db:
            print(customer)
        return True

    def modify_customer_info(self, filename):
        '''
        Method that modify or updates information only on certain records
        '''
        customers_to_update = read_from_json(filename)
        db = read_from_json(self.customer_filename)
        for customer in db:
            for c_update in customers_to_update:
                # Just update necesarry items, not all of them
                if customer['id'] == c_update['id']:
                    customer['id'] = c_update['id']
                    customer['first_name'] = c_update['first_name']
                    customer['last_name'] = c_update['last_name']
                    customer['phone_number'] = c_update['phone_number']
        self.customers = db
        write_to_json(self.customers)
        self.display_customer_info()
        return db


def delete_final_file(path='Customers.json'):
    '''
    Esta función elimina el archivo final en caso de existir
    para sobrescribirlo con cada ejecución
    '''
    if os.path.isfile(path):
        os.remove(path)


def read_from_json(filename='Customers.json'):
    '''
    Función encargada de leer el archivo de tipo json
    '''

    with open(filename, 'r', encoding='utf-8') as jsonfile:
        result = json.loads(jsonfile.read())
    return result


def write_to_json(customers, filepath='Customers.json'):
    '''
    Función encargada de escribir la información en archivo json
    '''
    with open(filepath, "w", encoding='utf-8') as outfile:
        json.dump(customers, outfile)


def main():
    '''
    Ejecución principal del programa
    '''
    start_time = time.time()
    hotels = Hotels()
    customers = Customers()

    print('Inicio de programa')
    # File mode
    try:
        mode = sys.argv[1]
        if mode[-1].upper() in ('C', 'R', 'U', 'D'):
            print(f'File will be oppened in mode: {mode[-1]}')
        else:
            print('Wrong file mode')
            return
    except (FileNotFoundError, IndexError) as error:
        print('Wrong file mode.', error)

    # Reading content from JSON files
    try:
        file_content = sys.argv[2]
        type_of_file = file_content.split("\\")[-1][0]
        if mode[-1].upper() == 'C':
            if type_of_file == "C":
                delete_final_file()
                customers.create(file_content)
            elif type_of_file == "H":
                delete_final_file('Hotels.json')
                hotels.create_all_hotels(file_content)
            print('Records created')
        elif mode[-1].upper() == 'U':
            if type_of_file == "C":
                customers.modify_customer_info(file_content)
            elif type_of_file == "H":
                hotels.modify_hotel_info(file_content)
            print('Records updated')
        elif mode[-1].upper() == 'D':
            customers.delete_customer(file_content)
            print('Records deleted')
        final_time = time.time()
        print(f'Tiempo de execucion en segundos: {final_time-start_time}')
        print('Fin de execución')
    except (FileNotFoundError, IndexError) as error:
        print('No file was found', error)


if __name__ == '__main__':
    main()
