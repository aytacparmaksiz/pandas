"""Dataset Structure
The dataset will have the following columns:

Date: The date of the sales record.
Region: The region where the sales occurred.
Fruit_Type: The type of fruit (e.g., Apple, Orange, Banana).
Size: The size of the fruit (e.g., Small, Medium, Large).
Price: The price per unit of the fruit.
Units_Sold: The number of units sold.
Total_Revenue: The total revenue from the sales. """


import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Date': pd.date_range(start='2023-01-01', periods=100, freq='W'),
    'Region': ['North', 'South', 'East', 'West'] * 25,
    'Fruit_Type': ['Apple', 'Orange', 'Banana', 'Apple', 'Orange', 'Banana'] * 16 + ['Apple', 'Orange', 'Banana', 'Apple'],
    'Size': ['Small', 'Medium', 'Large'] * 33 + ['Small'],
    'Price': [0.5, 0.7, 0.9, 0.6, 0.8, 1.0] * 16 + [0.5, 0.7, 0.9, 0.6],
    'Units_Sold': [200, 180, 220, 240, 260, 210] * 16 + [200, 180, 220, 240],
}

# Calculate Total_Revenue
data['Total_Revenue'] = [p * u for p, u in zip(data['Price'], data['Units_Sold'])]

# Create DataFrame
df = pd.DataFrame(data)

# Question 1: Create a plot that shows the total revenue over time

df.groupby('Date')['Total_Revenue'].sum().plot(figsize= (10, 6), title='Total Revenue Over Time')
plt.ylabel('Total Revenue')
plt.show()

# Question 2: Determine the most popular fruit size based on the number of units sold.

popular_size = df.groupby('Size')['Units_Sold'].sum().idxmax() # The answer is small.

# Question 3: Analyze the change in sales over time for a specific fruit type, such as apples.

apple_sales_over_time = df[df["Fruit_Type"] == "Apple"].groupby('Date')["Units_Sold"].sum()
apple_sales_over_time.plot(figsize = (10,5), title = "Apple Sales Over Time")
plt.ylabel('Units_Sold')
plt.show()

# Question 4: Analyze the relationship between the price of a fruit and the number of units sold.

# Scatter chart can only be used in DataFrame.plot() method, groupby() creates a series and therefore new DF as df_grouped has been created.
df_grouped = df.groupby('Price')['Units_Sold'].sum().reset_index()
df_grouped.plot(x = 'Price', y = 'Units_Sold', kind = 'scatter')
plt.show()

# Question 5: Find, remove, and replace missing values in the dataset.

# Find missing values
missing_values = df.isnull().sum()
print("Missing values in each column:\n", missing_values)

# Remove rows with missing values
df_cleaned = df.dropna()

# Replace missing values with 0
df_filled = df.fillna({'Price': df['Price'].mean()})

# Question 5: Find out which fruit type has the highest total units sold.

highest_selling_fruit = df.groupby("Fruit_Type")["Units_Sold"].sum().idxmax()
print("The most sold fruit is {}.".format(highest_selling_fruit))

# Question 6: Which region has the highest average selling price?

highest_avg_price = df.groupby('Region')['Price'].mean().idxmax()
print("The region with the highest average price is {}.".format(highest_avg_price))

# Question 7: What is the distribution of fruit sizes sold in different regions?

size_distribution_by_region = df.pivot_table(values = 'Units_Sold', index = ('Size'), columns = 'Region', aggfunc = 'sum')
print(size_distribution_by_region)


# Question 8: Which fruit type generated the highest total revenue?

top_revenue_fruit = df.groupby("Fruit_Type")['Total_Revenue'].sum().idxmax()
print("The fruit with the highest total revenue is {}.". format(top_revenue_fruit))

# Question 9: Do sales exhibit seasonal patterns over the year?

df['Month'] = df['Date'].dt.month
seasonal_sales = df.groupby('Month')["Units_Sold"].sum()
seasonal_sales.plot(kind = 'bar', title = "Seasonal Sales Distribution")
plt.xlabel('Month')
plt.ylabel('Units Sold')
plt.show()

# Question 10: How have total units sold changed over time?

total_units_sold_over_time = df.groupby('Date')['Units_Sold'].sum().plot(kind = 'line', title = 'Total Units Sold Over Time')
plt.ylabel('Units Sold')
plt.show()

# Question 11: What is the average price for each fruit type?

avg_prices_each_fruit = df.groupby('Fruit_Type')['Price'].mean().reset_index()

# Created a bar char to visualize the average prices of each fruit type.

avg_prices_each_fruit.plot(kind = 'bar', x='Fruit_Type', y='Price', title = 'Average Prices of Each Fruit Type', legend = False)
plt.xlabel('Fruit Type')
plt.ylabel('Price')
plt.show()

# Question 12: Which region has the highest total units sold?

units_sold_by_region = df.groupby('Region')['Units_Sold'].sum().reset_index()

# Created a bar char to visualize to see which region has the highest total units sold.

units_sold_by_region.plot(kind='bar', x ='Region', y='Units_Sold', title = 'Units Sold by Region', legend = False, color = 'red')
plt.xlabel('Region')
plt.ylabel('Units Sold')
plt.show()

# Question 13: What is the distribution of prices for the products?

df['Price'].plot(kind = 'hist', bins = 30, title = 'Price Distribution', color = "green")
plt.xlabel('Prices')
plt.ylabel('Frequency')
plt.show()

# Question 14: Is there a correlation between price and units sold?

df.plot(kind = 'scatter', x = 'Price', y = 'Units_Sold', title='Price vs Units Sold')
plt.xlabel('Price')
plt.ylabel('Units Sold')
plt.show()

#There is no correlation betweeen price and units sold.

# Question 15: How are sales distributed across different fruit types and regions?

# Pivot table for Units Sold by Fruit_Type and Region
sales_distribution = df.pivot_table(values = 'Units_Sold', index = 'Fruit_Type', columns ='Region', aggfunc = 'sum')

# Plotting the pivot table
sales_distribution.plot(kind = 'bar', stacked =True, title = 'Sales Breakdown by Fruit Type and Region',legend = False)
plt.xlabel('Fruit Type')
plt.ylabel('Units Sold')
plt.show()




