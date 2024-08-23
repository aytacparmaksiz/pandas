import pandas as pd

# Creating the dataset
data = {
    'Product': ['Laptop', 'Smartphone', 'Tablet', 'Monitor', 'Keyboard', 'Mouse', 'Printer', 'Headphones'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Accessories', 'Accessories', 'Accessories', 'Electronics', 'Accessories'],
    'Date': pd.to_datetime(['2024-08-01', '2024-08-01', '2024-08-02', '2024-08-02', '2024-08-03', '2024-08-03', '2024-08-04', '2024-08-04']),
    'Price': [1200, 800, 300, 200, 50, 30, 150, 100],
    'Quantity': [10, 15, 8, 12, 20, 25, 5, 18]
}

df = pd.DataFrame(data)
df.set_index('Product', inplace=True)
print(df)

# Question 1: Display all the details for the product "Tablet."

df.loc["Tablet"]

# Question 2: Display the prices for "Smartphone," "Monitor," and "Mouse."

df.loc[["Smartphone", "Monitor", "Mouse"],"Price"]

# Question 3: Sort the DataFrame by the "Product" index alphabetically.

df.sort_index(level = 'Product', ascending = True)

# Question 4: Set the "Date" column as the new index.

df = df.reset_index()
df = df.set_index("Date")

# Question 5: Display the "Price" and "Quantity" for all products sold on "2024-08-02."

df.loc["2024-08-02", ["Price", "Quantity"]]

# Question 6: Use .iloc[] to select the first three rows of the DataFrame.

df.iloc[0:3]

# Question 7: Select all products sold in August 2024 using .loc[].

df.loc["2024-08"]

# Question 8: Use .iloc[] to select the last two rows of the DataFrame.

df.iloc[-2:]
