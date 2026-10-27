import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px

# Load the dataset
df = pd.read_csv('supply_chain_data.csv')

# Data Preprocessing

# Check for missing values
missing_values = df.isnull().sum()
print("Missing Values:\n", missing_values)

# Displaying the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Displaying information about the dataset (columns, data types, non-null counts)
print("\nDataset Information:")
df.info()

# Displaying the data types of the columns
print("\nData types of columns:")
print(df.dtypes)

# Checking the shape of the dataset (rows, columns)
print("\nShape of the dataset (rows, columns):")
print(df.shape)

# Checking for duplicate rows in the dataset
print("\nAre there any duplicate rows?:")
duplicates = df.duplicated().any()
print(duplicates)

# If duplicates exist, remove them
if duplicates:
    df = df.drop_duplicates()

# Displaying the index of the dataframe
print("\nIndex of the dataframe:")
print(df.index)

# Displaying the columns of the dataframe
print("\nColumns of the dataframe:")
print(df.columns)

# Ensure numeric columns are in the correct data types
numeric_columns = ['Price', 'Revenue generated', 'Stock levels', 'Lead times', 
                   'Order quantities', 'Shipping times', 'Shipping costs', 
                   'Manufacturing costs', 'Defect rates', 'Production volumes', 'Costs']
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Standardizing categorical columns by stripping leading/trailing spaces and converting to lowercase
df['Product type'] = df['Product type'].str.strip().str.lower()
df['Supplier name'] = df['Supplier name'].str.strip().str.lower()
df['Location'] = df['Location'].str.strip().str.lower()

# Example: Detecting outliers using IQR for 'Price', 'Revenue generated', and 'Manufacturing costs'
Q1 = df[['Price', 'Revenue generated', 'Manufacturing costs']].quantile(0.25)
Q3 = df[['Price', 'Revenue generated', 'Manufacturing costs']].quantile(0.75)
IQR = Q3 - Q1

# Identifying outliers: Data points that are outside 1.5 * IQR range
outliers = (df[['Price', 'Revenue generated', 'Manufacturing costs']] < (Q1 - 1.5 * IQR)) | \
           (df[['Price', 'Revenue generated', 'Manufacturing costs']] > (Q3 + 1.5 * IQR))

# Displaying outliers
print("\nOutliers found in the dataset (True means outliers present):")
print(outliers.any())

# Example: Checking unique values in 'Customer demographics'
print("\nUnique values in 'Customer demographics':")
print(df['Customer demographics'].unique())

# Example: Ensuring 'Defect rates' are within the expected range (0 to 1)
invalid_defect_rates = df[(df['Defect rates'] < 0) | (df['Defect rates'] > 1)]
print("\nInvalid Defect rates (if any):")
print(invalid_defect_rates)


# Converting 'Costs' and other columns to appropriate data types
df['Costs'] = pd.to_numeric(df['Costs'], errors='coerce')
df['Price'] = df['Price'].astype(float)
df['Availability'] = df['Availability'].astype(int)


 # Profit Margin: (Revenue - Manufacturing Costs) / Revenue
df['Profit Margin'] = (df['Revenue generated'] - df['Manufacturing costs']) / df['Revenue generated']

# Price-to-Revenue Ratio: Price / Revenue
df['Price to Revenue Ratio'] = df['Price'] / df['Revenue generated']

# Lead Time Efficiency: Lead Times / Shipping Times
df['Lead Time Efficiency'] = df['Lead times'] / df['Shipping times']

# Shipping Cost per Unit: Shipping Costs / Order Quantities
df['Shipping Cost per Unit'] = df['Shipping costs'] / df['Order quantities']

# Days in Inventory: Stock Levels / Order Quantities
df['Days in Inventory'] = df['Stock levels'] / df['Order quantities']

# Defect Rate per Production Volume: Defect Rates / Production Volumes
df['Defect Rate per Production Volume'] = df['Defect rates'] / df['Production volumes']

# Revenue per Product Type: Group by Product Type and sum of Revenue
df['Revenue per Product Type'] = df.groupby('Product type')['Revenue generated'].transform('sum')

# Average Shipping Time per Carrier: Group by Shipping Carrier and mean of Shipping Times
df['Average Shipping Time per Carrier'] = df.groupby('Shipping carriers')['Shipping times'].transform('mean')

# Manufacturing Cost per Unit: Manufacturing Costs / Production Volumes
df['Manufacturing Cost per Unit'] = df['Manufacturing costs'] / df['Production volumes']

# Stock Turnover Rate: Order Quantities / Stock Levels
df['Stock Turnover Rate'] = df['Order quantities'] / df['Stock levels']

# Cost to Revenue Ratio: Costs / Revenue
df['Cost to Revenue Ratio'] = df['Costs'] / df['Revenue generated']

# Visualization
# Plot histograms for numerical features
df[numeric_columns].hist(bins=20, figsize=(14, 10), layout=(4, 3))
plt.suptitle('Distribution of Numerical Features')
plt.show()

# Boxplots to check for outliers in the numerical features
for col in numeric_columns:
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=df[col])
    plt.title(f'Boxplot of {col}')
    plt.show()

# Correlation heatmap to see relationships between numerical variables
plt.figure(figsize=(10, 8))
sns.heatmap(df[numeric_columns].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap of Numerical Features")
plt.show()

# Distribution of categorical variables (e.g., 'Product type', 'Shipping carriers', 'Supplier name')
categorical_cols = ['Product type', 'Shipping carriers', 'Supplier name', 'Location']

for col in categorical_cols:
    plt.figure(figsize=(8, 5))
    sns.countplot(x=df[col], palette='viridis')
    plt.title(f'Distribution of {col}')
    plt.show()

# Price vs. Revenue
plt.figure(figsize=(8, 6))
sns.scatterplot(y=df['Price'], x=df['Revenue generated'])
plt.title('Price vs Revenue Generated')
plt.xlabel('Price')
plt.ylabel('Revenue Generated')
plt.show()

#Stock Levels vs. Order Quantities
plt.figure(figsize=(8, 6))
sns.scatterplot(y=df['Stock levels'], x=df['Order quantities'])
plt.title('Stock Levels vs Order Quantities')
plt.xlabel('Stock Levels')
plt.ylabel('Order Quantities')
plt.show()

#Manufacturing Costs vs. Defect Rates
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df['Manufacturing costs'], y=df['Defect rates'])
plt.title('Manufacturing Costs vs Defect Rates')
plt.xlabel('Manufacturing Costs')
plt.ylabel('Defect Rates')
plt.show()

#Insights into Product Performance
plt.figure(figsize=(10, 6))
sns.barplot(x=df['Revenue per Product Type'].value_counts().index, 
            y=df['Revenue per Product Type'].value_counts().values)
plt.title('Revenue per Product Type')
plt.xlabel('Product Type')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.show()

# Shipping Performance Analysis
plt.figure(figsize=(10, 6))
sns.barplot(x=df['Average Shipping Time per Carrier'].value_counts().index, 
            y=df['Average Shipping Time per Carrier'].value_counts().values)
plt.title('Average Shipping Time per Carrier')
plt.xlabel('Carrier')
plt.ylabel('Average Shipping Time')
plt.xticks(rotation=45)
plt.show()

# Plotting Lead Time Efficiency
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df['Lead Time Efficiency'], y=df['Revenue generated'])
plt.title('Lead Time Efficiency vs Revenue Generated')
plt.xlabel('Lead Time Efficiency')
plt.ylabel('Revenue Generated')
plt.show()

# Final Data Overview
print("\nData after cleaning:")
print(df.info())

df.to_csv('cleaned_supply_chain_data.csv', index=False)
