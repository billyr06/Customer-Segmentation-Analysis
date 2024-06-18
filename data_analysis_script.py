import pandas as pd
from dotenv import load_dotenv
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Load environment variables from .env file
load_dotenv()

# Get the file paths from environment variables
list_of_orders_path = os.getenv('LIST_OF_ORDERS_PATH')
order_details_path = os.getenv('ORDER_DETAILS_PATH')
sales_target_path = os.getenv('SALES_TARGET_PATH')

# Check if file paths are loaded correctly
if not list_of_orders_path or not order_details_path or not sales_target_path:
    raise ValueError("One or more file paths not found. Please check your .env file")

# Load the datasets
list_of_orders = pd.read_csv(list_of_orders_path)
order_details = pd.read_csv(order_details_path)
sales_target = pd.read_csv(sales_target_path)

# Display basic information and summary statistics
print("List of Orders Info:")
print(list_of_orders.info(), "\n")
print("List of Orders Summary Statistics:")
print(list_of_orders.describe(), "\n")

print("Order Details Info:")
print(order_details.info(), "\n")
print("Order Details Summary Statistics:")
print(order_details.describe(), "\n")

print("Sales Target Info:")
print(sales_target.info(), "\n")
print("Sales Target Summary Statistics:")
print(sales_target.describe(), "\n")

# Identify missing values
print("Missing Values in List of Orders:")
print(list_of_orders.isnull().sum(), "\n")

print("Missing Values in Order Details:")
print(order_details.isnull().sum(), "\n")

print("Missing Values in Sales Target:")
print(sales_target.isnull().sum(), "\n")

# Example strategy: drop rows with missing values
list_of_orders_cleaned = list_of_orders.dropna()
order_details_cleaned = order_details.dropna()
sales_target_cleaned = sales_target.dropna()

# Check for duplicates
print("Duplicates in List of Orders:", list_of_orders.duplicated().sum(), "\n")
print("Duplicates in Order Details:", order_details.duplicated().sum(), "\n")
print("Duplicates in Sales Target:", sales_target.duplicated().sum(), "\n")

# Remove duplicates
list_of_orders_cleaned = list_of_orders_cleaned.drop_duplicates()
order_details_cleaned = order_details_cleaned.drop_duplicates()
sales_target_cleaned = sales_target_cleaned.drop_duplicates()

# Convert date columns to datetime where applicable
list_of_orders_cleaned['Order Date'] = pd.to_datetime(list_of_orders_cleaned['Order Date'], format='%d-%m-%Y', dayfirst=True, errors='coerce')

# Generate histograms for numerical columns
list_of_orders_cleaned.hist(figsize=(10, 8))
plt.suptitle('List of Orders - Histograms')
plt.savefig('list_of_orders_histograms.png')

order_details_cleaned.hist(figsize=(10, 8))
plt.suptitle('Order Details - Histograms')
plt.savefig('order_details_histograms.png')

sales_target_cleaned.hist(figsize=(10, 8))
plt.suptitle('Sales Target - Histograms')
plt.savefig('sales_target_histograms.png')

# Generate correlation heatmaps for numeric columns only
def plot_heatmap(dataframe, title, filename):
    numeric_df = dataframe.select_dtypes(include=['number'])
    if not numeric_df.empty:
        plt.figure(figsize=(10, 8))
        sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
        plt.title(title)
        plt.savefig(filename)
    else:
        print(f"No numeric columns to plot heatmap for {title}")

plot_heatmap(list_of_orders_cleaned, 'List of Orders - Correlation Heatmap', 'list_of_orders_corr_heatmap.png')
plot_heatmap(order_details_cleaned, 'Order Details - Correlation Heatmap', 'order_details_corr_heatmap.png')
plot_heatmap(sales_target_cleaned, 'Sales Target - Correlation Heatmap', 'sales_target_corr_heatmap.png')
