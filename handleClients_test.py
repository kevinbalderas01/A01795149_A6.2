import unittest
import coverage
from handleClients import Customers
from handleClients import write_to_json, read_from_json


class testCustomers(unittest.TestCase):
    customers = Customers()
    filename = r"C:\Users\balde\Desktop\MOOCS\A01795149_A6.2\Files\Customer_create.json"
    filename_delete = r"C:\Users\balde\Desktop\MOOCS\A01795149_A6.2\Files\Customer_delete.json"
    filename_update = r"C:\Users\balde\Desktop\MOOCS\A01795149_A6.2\Files\Customer_update.json"
    def test_generate_id(self):
        self.assertEqual(self.customers.generate_id(),7)
        self.assertEqual(self.customers.generate_id(),8)
        self.assertEqual(self.customers.generate_id(),9)
    def test_create(self):
        new= self.customers.create(self.filename)
        old = [{'first_name': 'Kevin', 'last_name': 'Balderas', 'phone_number': '554789845'}, 
               {'first_name': 'Juan', 'last_name': 'Sanchez', 'phone_number': '5587985487'}, 
               {'first_name': 'Daniel', 'last_name': 'Gomez', 'phone_number': '98764577'}, 
               {'first_name': 'Jesus', 'last_name': 'Hernandez', 'phone_number': '154879895'}, 
               {'first_name': 'Alexis', 'last_name': 'Mejia', 'phone_number': '65874587'}]
        self.assertListEqual(new, old)
    def test_create_customer(self):
        new_customer = self.customers.create_customer('Jake', 'Martinez', '879876574')
        self.assertDictEqual(new_customer, {'id':6,'first_name':'Jake', 'last_name':'Martinez', 'phone_number':'879876574'})

    def test_delete_customer(self):
        to_not_delete = self.customers.delete_customer(self.filename_delete)
        new = [{'id': 3, 'first_name': 'Daniel', 'last_name': 'Gomez', 'phone_number': '98764577'}, {'id': 4, 'first_name': 'Jesus', 'last_name': 'Hernandez', 'phone_number': '154879895'}, {'id': 5, 'first_name': 'Alexis', 'last_name': 'Mejia', 'phone_number': '65874587'}]
        self.assertListEqual(to_not_delete, new)

    def test_modify_customer_info(self):
        to_update = self.customers.modify_customer_info(self.filename_update)
        new = [{'id': 3, 'first_name': 'Daniel', 'last_name': 'Gomez', 'phone_number': '98764577'}, {'id': 4, 'first_name': 'Jesus Gallego', 'last_name': 'Hernandez', 'phone_number': '58474'}, {'id': 5, 'first_name': 'Alexis Augusto', 'last_name': 'Mejia', 'phone_number': '12354'}]
        self.assertListEqual(to_update, new)

    def test_display_customer_info(self):
        self.assertTrue(self.customers.display_customer_info())
    
    def test_read_from_json(self):
        result = read_from_json()
        print(result)
        truth = [{'id': 3, 'first_name': 'Daniel', 'last_name': 'Gomez', 'phone_number': '98764577'}, {'id': 4, 'first_name': 'Jesus Gallego', 'last_name': 'Hernandez', 'phone_number': '58474'}, {'id': 5, 'first_name': 'Alexis Augusto', 'last_name': 'Mejia', 'phone_number': '12354'}]
        self.assertListEqual(result, truth)

   

if __name__ == '__main__':
    cov = coverage.Coverage()
    cov.start()

    try:
        unittest.main()
    except:  # catch-all except clause
        pass

    cov.stop()
    cov.save()

    cov.html_report()
    print("Done.")