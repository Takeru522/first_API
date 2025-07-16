import requests

url = "https://fakestoreapi.com/products"
response = requests.get(url)
products = response.json()

print(products[0])  # show the first product
#  Step 3: Clean the Data with Pandas
import pandas as pd

df = pd.DataFrame(products)
df = df[['id', 'title', 'price', 'category']]
df.columns = ['product_id', 'product_name', 'price', 'category']

print(df.head())
#Step 4: Save It into a Database (Load)
import sqlite3

conn = sqlite3.connect("product_data.db")
df.to_sql("products", conn, if_exists="replace", index=False)
conn.close()