import pandas as pd

#Problem 1

data = {
    'Date': ['2024-08-01', '2024-08-01', '2024-08-02', '2024-08-02', '2024-08-03', '2024-08-03'],
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Clothing', 'Electronics', 'Clothing'],
    'Product': ['TV', 'Shirt', 'Phone', 'Jacket', 'TV', 'Shirt'],
    'Units Sold': [10, 20, 15, 5, 7, 12]
}

df = pd.DataFrame(data)

# Task 1: Group the data by Category and calculate the total units sold for each category.

unit_sold_by_cat = df.groupby("Category")["Units Sold"].sum()
print(unit_sold_by_cat)

# Task 2: Further group by Category and Product to find out the total units sold for each product.

unit_sold_by_cat_prd = df.groupby(["Category", "Product"])["Units Sold"].sum()
print(unit_sold_by_cat_prd)

# Problem 2

data2 = {
    'Department': ['HR', 'Finance', 'IT', 'Finance', 'IT', 'HR'],
    'Employee': ['John', 'Anna', 'Mike', 'Sophie', 'Tom', 'Sarah'],
    'Salary': [50000, 60000, 70000, 50000, 80000, 55000]
}

df = pd.DataFrame(data2)

#Task 1: Group the data by Department and calculate the average salary for each department.

avg_sal_by_dep = df.groupby("Department")["Salary"].mean()
print(avg_sal_by_dep)

#Task 2: Group by Department and find the maximum salary in each department.

max_salary = df.groupby("Department")["Salary"].max()
print(max_salary)

# Problem 3

data3 = {
    'Region': ['East', 'West', 'North', 'South', 'East', 'West', 'North', 'South'],
    'Salesperson': ['Alice', 'Bob', 'Charlie', 'David', 'Edward', 'Frank', 'George', 'Helen'],
    'Sales': [300, 200, 400, 500, 600, 700, 300, 400]
}

df = pd.DataFrame(data3)

#Task 1: Group the data by Region and calculate the total sales for each region.

total_sales_by_region = df.groupby("Region")["Sales"].sum()
print(total_sales_by_region)

#Task 2: Find the salesperson with the highest sales in each region.

max_salary_by_sp = df.loc[df.groupby("Region")["Sales"].idxmax()] #I used the idxmax() function to see the maximum values ​​on a Salesperson basis. df.loc was used to access group rows and columns.
print(max_salary_by_sp)


# Problem 4

import pandas as pd

data4 = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie'],
    'Department': ['Sales', 'Sales', 'Sales', 'Marketing', 'Marketing', 'Marketing', 'Sales', 'Sales', 'Sales', 'Marketing', 'Marketing', 'Marketing'],
    'Region': ['East', 'East', 'West', 'East', 'East', 'West', 'West', 'West', 'East', 'West', 'West', 'East'],
    'Month': ['2024-07', '2024-07', '2024-07', '2024-07', '2024-07', '2024-07', '2024-08', '2024-08', '2024-08', '2024-08', '2024-08', '2024-08'],
    'Sales': [2000, 1500, 2500, 3000, 2000, 4000, 2200, 1600, 2400, 3100, 2100, 4300],
    'Targets': [2500, 2000, 3000, 3500, 2500, 4500, 2700, 2100, 2900, 3500, 2300, 4700],
}

df = pd.DataFrame(data4)

#Task 1: Create a pivot table to calculate the total sales for each department in each region. Replace any missing values with 0.

total_sales_by_dep_reg = df.pivot_table(values = "Sales", index = "Department", columns ="Region", aggfunc = 'sum', fill_value = 0)
print(total_sales_by_dep_reg)

#Task 2: Create a pivot table to find the average sales per month for each employee. Include the grand total for both rows and columns.

avg_sales_per_month = df.pivot_table(values = "Sales", index = "Employee", columns ='Month', aggfunc = 'mean', margins = True)
print(avg_sales_per_month)

#Task 3: Create a pivot table to compare the total sales against the total targets for each department and each region. Add grand totals for both sales and targets.

sales_vs_targets = df.pivot_table(values = ["Sales", "Targets"], index = "Department", columns = "Region", aggfunc = 'sum', margins = True )
print(sales_vs_targets)

#Task 4: Create a pivot table that shows the percentage of the sales target achieved by each employee in each region. Replace any missing values with 0.

df["% of Target Achieved"] = (df["Sales"] / df["Targets"]) * 100
perc_of_target_achived = df.pivot_table(values = "% of Target Achieved", index = 'Employee', columns = 'Region', aggfunc = 'mean', fill_value = 0)
print(perc_of_target_achived)

#Task 5: Create a pivot table to identify the top-performing department in terms of average sales across all regions. Include the overall average sales for each department and region.

top_perf_dep = df.pivot_table(values = 'Sales', index = 'Department', columns = 'Region', aggfunc = 'mean', margins = True)
print(top_perf_dep)
