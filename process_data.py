# генерация транзакций
# import random
# import pandas as pd
# import csv


# ROWS_NUMBER = 10000
# PRODUCT_CATEGORIES_LIST = [
#     'drink', 
#     'furniture and decor', 
#     'fashion and apparel', 
#     'toys and hobbies', 
#     'pet products', 
#     'shoes', 
#     'cosmetics and bodycare',
#     'food and beverage',
#     'media',
#     'digital services',
#     'health and wellness',
#     'office equipment',
#     'electronics',
# ]

# def get_product_category():
#     return PRODUCT_CATEGORIES_LIST[random.randint(0,len(PRODUCT_CATEGORIES_LIST) - 1)]

# def get_date():
#     return str(random.randint(1,28)) + '-' + str(random.randint(1,12)) + '-2024'

# def get_products():
#     products = list()
#     for i in range(1000):
#         product = {
#             'product_id': random.randint(1,100000),
#             'product_category': get_product_category(),
#             'product_price': round(random.uniform(100, 10000), 2)
#         }
#         products.append(product)
    
#     return products

# rows = list()
# transaction_id = 0
# products_list = get_products()
# for i in range(ROWS_NUMBER):
#     row = dict()
#     transaction_id += 1
#     product = products_list[random.randint(0,len(products_list)-1)]
#     row['transaction_id'] = transaction_id
#     row['customer_id'] = random.randint(1, 100)
#     row['product_id'] = product['product_id']
#     row['product_category'] = product['product_category']
#     row['amount'] = product['product_price']
#     row['date'] = get_date()
#     rows.append(row)

# with open('transactions.csv', 'w') as myfile:
#      wr = csv.writer(myfile)
#      wr.writerow(rows[0].keys())
#      for i in range(ROWS_NUMBER):
#          wr.writerow(rows[i].values())

# обработка транзакций
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime


df = pd.read_csv('transactions.csv')
df_no_na = df.dropna()
df_no_na['date'] = df_no_na['date'].apply(lambda x: datetime.strptime(x, '%d-%m-%Y'))
transactions_count = len(df_no_na.index)
print(f'количество транзакций: {transactions_count}')
unique_clients = df_no_na['customer_id'].nunique()
print(f'уникальные клиенты: {unique_clients}')
print('топ-5 категорий продуктов по общему доходу:')
print(df_no_na.groupby(['product_category'])['amount'].sum().reset_index().sort_values('amount', ascending=False).head())
print('средняя сумма транзакции по каждой категории продуктов:')
print(df_no_na.groupby(['product_category'])['amount'].mean())

df_no_na['year_month'] = df_no_na['date'].apply(lambda x: ' '.join([str(x.year), str(x.month)]))

fig, axs = plt.subplots(1, 2)
axs[0].hist(df_no_na['year_month'])
df_for_pie = df_no_na.groupby(['product_category'])['amount'].sum().reset_index()
axs[1] = plt.pie(df_for_pie['amount'], labels=df_for_pie['product_category'])
plt.show()

new_df = df_no_na.groupby(['customer_id', 'year_month'])['amount'].sum().reset_index()
new_df.to_csv('monthly_revenue_per_customer.csv', index=False)