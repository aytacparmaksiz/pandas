import pandas as pd
import numpy as np

# Creating a sample dataset
data = {
    'OrderID': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010],
    'Product': ['Laptop', 'Smartphone', 'Tablet', 'Monitor', 'Keyboard', 'Mouse', 'Printer', 'Headphones', 'Smartwatch', 'Camera'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Accessories', 'Accessories', 'Accessories', 'Electronics', 'Accessories', 'Electronics', 'Electronics'],
    'OrderDate': pd.to_datetime(['2024-07-01', '2024-07-02', '2024-07-03', '2024-07-04', '2024-07-05', '2024-07-06', '2024-07-07', '2024-07-08', '2024-07-09', '2024-07-10']),
    'Sales': [1500, 800, 600, 300, 100, 50, 200, 150, 350, 900],
    'Quantity': [2, 5, 3, 10, 15, 20, 1, 8, 4, 7],
    'CustomerID': [501, 502, 503, 504, 505, 506, 507, 508, 509, 510]
}

df = pd.DataFrame(data)
print(df)

# Question 1: Set 'OrderID' as the index of the DataFrame.

df = df.set_index("OrderID") # or df.set_index("OrderID", inplace = True)

# Question 2: Remove 'OrderID' as the index and reset it back to a column.

df.reset_index(inplace = True)

# Question 3: Select orders where 'Category' is 'Electronics' using .loc[].

electronics = df.loc[df["Category"] == "Electronics"]

# Question 4: Set 'Category' and 'Product' as multi-level indexes.

df_multi_index = df.set_index(["Category", "Product"])

# Question 5: Sort the DataFrame by 'Sales' in descending order.

df.sort_values(by = "Sales", ascending = False)

# Question 6: Use .loc[] to select the rows for orders made between "2024-07-03" and "2024-07-07".

df.loc[(df["OrderDate"] >= "2024-07-03") & (df["OrderDate"] <= "2024-07-07")]

# Question 7: Select rows with index values from 3 to 6 using .iloc[].
df.iloc[3:7]

# Question 8: Select rows with index 2 to 5 and only columns 'Product', 'Sales', and 'Quantity' using .iloc[].

df.iloc[2:6, [1,4,5]]

# Question 9: Select orders made in July 2024.

df.loc[df["OrderDate"].dt.month == 7]

# Question 10: Select the 2nd and 4th row and columns 'Product' and 'Sales'.

df.iloc[[1,3], [1,4]]

# Question 11: Create a pivot table showing the total sales for each product category.

df.pivot_table(values = "Sales", index = "Category", aggfunc = 'sum')

# Question 12: Create a pivot table showing the total quantity of each product sold by each 'CustomerID'.

pivot_quantity = df.pivot_table(values='Quantity', index = 'Product', columns ='CustomerID', aggfunc = 'sum', fill_value = 0)

# Question 13: Subset the above pivot table to show only the 'Smartphone' and 'Tablet' sales for customers 502 and 503.

pivot_quantity.loc[["Smartphone","Tablet"], [502,503]]

# Question 14: Calculate the total quantity of products sold for each customer using the pivot table.

pivot_quantity.sum(axis = 0)
