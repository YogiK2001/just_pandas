# 1. Create DataFrames
import pandas as pd
import numpy as np

np.random.seed(42)

# Product Master Data
product_data = {
    'ProductID': [101, 102, 103, 104, 105, 106, 107, 108],
    'ProductName': ['Laptop', 'Smartphone', 'Jeans', 'T-Shirt', 'Rice', 'Wheat', 'Headphones', 'Microwave'],
    'Category': ['Electronics', 'Electronics', 'Clothing', 'Clothing', 'Grocery', 'Grocery', 'Electronics', 'Electronics'],
    'UnitPrice': [75000, np.nan, 1500, 800, 1200, 1000, 2500, np.nan],
    'Stock': [10, 25, 60, 30, 80, 40, 15, 5]
}
df_products = pd.DataFrame(product_data)

# Sales Data
sales_data = {
    'SaleID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 210],  # Note duplicate
    'ProductID': [101, 102, 103, 104, 105, 106, 107, 108, 101, 105, 105],
    'QuantitySold': [1, 2, 3, 2, 5, 1, 4, 1, 2, 3, 3],
    'SaleDate': ['2025-06-10', '2025-06-10', '2025-06-11', '2025-06-12', '2025-06-12',
                 '2025-06-13', '2025-06-13', '2025-06-14', '2025-06-14', '2025-06-15', '2025-06-15'],
    'CustomerType': ['Regular', 'Member', 'Regular', 'Member', 'Regular',
                     'Member', 'Member', 'Regular', 'Regular', 'Member', 'Member']
}
df_sales = pd.DataFrame(sales_data)
df_sales['SaleDate'] = pd.to_datetime(df_sales['SaleDate'])

# 2. Fill missing 'UnitPrice' with category-wise average
df_products['UnitPrice'] = df_products.groupby('Category')['UnitPrice'].transform(
    lambda x: x.fillna(x.mean())
)

# 3. Remove duplicate sales records
df_sales = df_sales.drop_duplicates()

# 4. Replace 'CustomerType' values
df_sales['CustomerType'] = df_sales['CustomerType'].replace({'Regular': 'R', 'Member': 'M'})
