import pandas as pd

df = pd.read_csv("sales_data.csv")

print("First 5 rows of the sales data::")
print(df.head())


print("\nDATASET SHAPE")
print(df.shape)

print("\nCOLUMN NAMES")
print(df.columns)

print("\nDATA TYPES")
print(df.dtypes)

print("\nSTATISTICAL SUMMARY")
print(df.describe())

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nDUPLICATE ROWS")
print(df.duplicated().sum())


df = df.drop_duplicates()

df = df.fillna(0)

print("\nDATA AFTER CLEANING")
print(df.head())

print("\nMISSING VALUES AFTER CLEANING")
print(df.isnull().sum())

print("\nDUPLICATE ROWS AFTER CLEANING")
print(df.duplicated().sum())

print("\nCOLUMN NAMES")
print(df.columns.tolist())



#================================================
#               SALES ANALYSIS                   
#================================================

total_revenue = df["Total_Sales"].sum()

total_quantity = df["Quantity"].sum()

average_sale = df["Total_Sales"].mean()

product_quantity = df.groupby("Product")["Quantity"].sum()
best_selling_product = product_quantity.idxmax()
best_selling_quantity = product_quantity.max()

product_revenue = df.groupby("Product")["Total_Sales"].sum()

highest_revenue_product = product_revenue.idxmax()
highest_product_revenue = product_revenue.max()

print("\n" + "=" * 50)
print("          SALES ANALYSIS          ")
print("=" * 50)

print(f"Total Revenue:: ${total_revenue:,.2f}")
print(f"Total Quantity Sold:: {total_quantity:,}")
print(f"Average Sale:: ${average_sale:,.2f}")

print(f"Best Selling Product:: {best_selling_product}")
print(f"Quantity Sold:: {best_selling_quantity}")

print(f"Highest Revenue Product:: {highest_revenue_product}")
print(f"Revenue Generated:: ${highest_product_revenue:,.2f}")

print("=" * 50)
