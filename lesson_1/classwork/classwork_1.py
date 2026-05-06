## 1. Why do companies analyze large volumes of data?
#  To make better decisions — understanding sales trends, customer behavior, and market changes to reduce costs and increase revenue.

# 2. How can Python help compared to Excel?
# Python processes millions of rows in seconds, cleans data automatically, and handles repetitive tasks with scripts — while Excel slows down or crashes.

# 3. How would I analyze 10,000 daily transactions?
# Load and clean the data
# Remove duplicates and incorrect values
# Find top-selling products, regions, and time periods
# Build charts to visualize the results

# 4. What tasks is Python useful for in BI?
# Data cleaning — fixing empty or incorrect values
# Visualization — creating charts and dashboards
# Automation — generating reports automatically
# Forecasting — predicting future trends with ML models

# 5. How to compare yearly profit using only Python:
profit = {
    2021: 150_000_000,
    2022: 200_000_000,
    2023: 175_000_000,
    2024: 220_000_000,
}

print("Year  | Profit")
print("-" * 25)
for year, amount in profit.items():
    print(f"{year}  | {amount:,} USD")

best_year = max(profit, key=profit.get)
print(f"\nMost profitable year: {best_year}")


# 6. What difficulties arise without knowing Python?
# Working with large data becomes slow and error-prone
# Everything must be done manually
# Complex analysis like forecasting becomes impossible
# You fall behind competitors technologically