import pandas as pd
import matplotlib.pyplot as plt

# Load data from Excel file
df = pd.read_excel("./source data/fuel-prices.xlsx", parse_dates=["DateTime"])

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(
    df["DateTime"],
    df["Price"],
    linestyle="-",
    color="b",
    label="Freight Price",
)
plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Freight Price Over Time")
plt.legend()
plt.grid()
plt.xticks(rotation=45)
plt.show()
