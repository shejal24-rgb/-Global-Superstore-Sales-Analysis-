import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

file_path = Path(__file__).parent / "ProjectDA" / "global_superstore.csv"

df = pd.read_csv("global_superstore.csv")

df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Month"] = df["Order_Date"].dt.month_name()
df["Profit_Margin"] = np.where(
    df["Sales"] > 0,
    (df["Profit"] / df["Sales"]) * 100,
    0
)

print(df.head())
print(df.info())
print(df.describe())

print("Total Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())
print("Total Orders:", df["Order_ID"].nunique())
print("Average Sales:", df["Sales"].mean())
print("Average Profit:", df["Profit"].mean())
print("Average Profit Margin:", df["Profit_Margin"].mean())

print(df.groupby("Region")["Sales"].sum())
print(df.groupby("Category")["Profit"].sum())
print(df.groupby("Segment")["Sales"].sum())

monthly_sales = df.groupby("Month")["Sales"].sum()
category_sales = df.groupby("Category")["Sales"].sum()
region_profit = df.groupby("Region")["Profit"].sum()

plt.figure(figsize=(9, 5))
sns.barplot(data=df, x="Category", y="Sales", estimator=sum)
plt.title("Sales by Product Category")
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()

plt.figure(figsize=(9, 5))
sns.barplot(data=df, x="Region", y="Sales", estimator=sum)
plt.title("Sales by Region")
plt.tight_layout()
plt.show()

plt.figure(figsize=(9, 5))
sns.barplot(data=df, x="Segment", y="Sales", estimator=sum)
plt.title("Sales by Customer Segment")
plt.tight_layout()
plt.show()

plt.figure(figsize=(9, 5))
sns.barplot(data=df, x="Category", y="Profit", estimator=sum)
plt.title("Profit by Product Category")
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()

plt.figure(figsize=(9, 5))
sns.lineplot(data=df, x="Order_Date", y="Sales", marker="o")
plt.title("Sales Trend Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(9, 5))
sns.scatterplot(data=df, x="Sales", y="Profit", hue="Category")
plt.title("Sales vs Profit")
plt.tight_layout()
plt.show()