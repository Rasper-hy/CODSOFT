# Sales Prediction - No installation needed
# Rule-based version (no ML libraries)

import csv
import urllib.request

# 1. Load dataset from GitHub (Advertising dataset)
url = "https://raw.githubusercontent.com/selva86/datasets/master/Advertising.csv"
response = urllib.request.urlopen(url)
lines = [l.decode('utf-8') for l in response.readlines()]
data = list(csv.DictReader(lines))

# 2. Convert Sales column to float
sales = [float(row["Sales"]) for row in data]

# 3. Calculate average sales growth rate
growth_rates = []
for i in range(1, len(sales)):
    growth_rates.append((sales[i] - sales[i-1]) / sales[i-1])
avg_growth = sum(growth_rates) / len(growth_rates)

# 4. Predict next sales value
last_sales = sales[-1]
predicted_sales = last_sales * (1 + avg_growth)

print(f"Average Growth Rate: {avg_growth:.2%}")
print(f"Predicted Next Month Sales: {predicted_sales:.2f} units")

# 5. Test prediction with sample ad spend
sample_spend = {"TV": 150, "Radio": 25, "Newspaper": 20}
print("Sample prediction (simple rule):", round(predicted_sales, 2))
