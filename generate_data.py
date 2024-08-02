import random
import pandas as pd
import csv


ROWS_NUMBER = 10000
PRODUCT_CATEGORIES_LIST = [
    'drink', 
    'furniture and decor', 
    'fashion and apparel', 
    'toys and hobbies', 
    'pet products', 
    'shoes', 
    'cosmetics and bodycare',
    'food and beverage',
    'media',
    'digital services',
    'health and wellness',
    'office equipment',
    'electronics',
]

def get_product_category():
    return PRODUCT_CATEGORIES_LIST[random.randint(0,len(PRODUCT_CATEGORIES_LIST) - 1)]

def get_date():
    return str(random.randint(1,28)) + '-' + str(random.randint(1,12)) + '-2024'

def get_products():
    products = list()
    for i in range(1000):
        product = {
            'product_id': random.randint(1,100000),
            'product_category': get_product_category(),
            'product_price': round(random.uniform(100, 10000), 2)
        }
        products.append(product)
    
    return products

rows = list()
transaction_id = 0
products_list = get_products()
for i in range(ROWS_NUMBER):
    row = dict()
    transaction_id += 1
    product = products_list[random.randint(0,len(products_list)-1)]
    row['transaction_id'] = transaction_id
    row['customer_id'] = random.randint(1, 100)
    row['product_id'] = product['product_id']
    row['product_category'] = product['product_category']
    row['amount'] = product['product_price']
    row['date'] = get_date()
    rows.append(row)

with open('transactions.csv', 'w') as myfile:
     wr = csv.writer(myfile)
     wr.writerow(rows[0].keys())
     for i in range(ROWS_NUMBER):
         wr.writerow(rows[i].values())