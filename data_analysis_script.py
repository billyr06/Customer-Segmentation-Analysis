import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the file path from environment variables
list_of_orders_path = os.getenv('LIST_OF_ORDERS_PATH')
order_details_path = os.getenv('ORDER_DETAILS_PATH')
sales_target_path = os.getenv('SALES_TARGET_PATH')

# Check if file paths are loaded correctly
if not list_of_orders_path or not order_details_path or not sales_target_path:
    raise ValueError("One or more file paths not found. Please check your .env file")

# Load datasets
list_of_orders = pd.read_csv(list_of_orders_path)
order_details = pd.read_csv(order_details_path)
sales_target = pd.read_csv(sales_target_path)

# Display the first few rows of each dataset
print("List of Orders:")
print(list_of_orders.head())

print("\nOrder Details:")
print(order_details.head())

print("\nSales Target:")
print(sales_target.head())
