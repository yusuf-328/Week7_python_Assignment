import pandas as pd
import matplotlib.pyplot as plt

# --- Load dataset ---
data = pd.read_csv("data.csv")
print("✅ Data loaded successfully\n")
print(data.head())

# --- Basic Analysis ---
print("\n--- Summary Statistics ---")
print(data.describe())

print("\n--- Total Sales by Region ---")
total_sales = data.groupby("Region")["Sales"].sum()
print(total_sales)

print("\n--- Average Sales by Month ---")
avg_sales = data.groupby("Month")["Sales"].mean()
print(avg_sales)

# --- Visualization 1: Bar Chart (Total Sales by Region) ---
plt.figure(figsize=(6,4))
total_sales.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Total Sales by Region")
plt.ylabel("Sales")
plt.xlabel("Region")
plt.show()

# --- Visualization 2: Line Chart (Average Sales per Month) ---
plt.figure(figsize=(6,4))
avg_sales.plot(kind="line", marker="o", color="green")
plt.title("Average Sales per Month")
plt.ylabel("Average Sales")
plt.xlabel("Month")
plt.grid(True)
plt.show()

# --- Visualization 3: Pie Chart (Sales Distribution by Region) ---
plt.figure(figsize=(5,5))
total_sales.plot(kind="pie", autopct="%1.1f%%", startangle=90, shadow=True)
plt.title("Sales Distribution by Region")
plt.ylabel("")
plt.show()