import pandas as pd

df = pd.read_csv("sales_data.csv")

print(df.head())

print(df.info())

print(df.shape)

print(df.isnull().sum())

df.drop_duplicates(inplace=True)

df.fillna(0, inplace=True)

df["Total_Sales"] = df["Quantity"] * df["Price"]

total_revenue = df["Total_Sales"].sum()

best_product = df.groupby("Product")["Quantity"].sum().idxmax()

average_sales = df["Total_Sales"].mean()

highest_sale = df["Total_Sales"].max()

lowest_sale = df["Total_Sales"].min()

print("Sales Analysis Report")

print(f"Total Revenue: ₹{total_revenue}")

print(f"Best Selling Product: {best_product}")

print(f"Average Sale Value: ₹{average_sales}")

print(f"Highest Sale: ₹{highest_sale}")

print(f"Lowest Sale: ₹{lowest_sale}")

