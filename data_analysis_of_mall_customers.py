'''
This project involves a detailed analysis of a dataset containing information about customers from a mall,
including their gender, age, annual income, and spending score. 
The project covers various data analysis techniques using Python and Pandas, 
including data inspection, sorting, subsetting, grouping, pivot tables, handling missing values, 
and data visualization using Matplotlib.

Dataset Name: Mall Customers
Source: https://www.kaggle.com/vjchoudhary7/customer-segmentation-tutorial-in-python
'''

# Load the dataset
import pandas as pd
df = pd.read_csv('Mall_Customers.csv')

# Question 1: Inspect the Mall Customers dataset and obtain general information about the DataFrame.
df.head()
df.info()
df.describe()

# Question 2: Sort the DataFrame based on customers' annual income and create a subset including only customers with an income above $60,000.

sorted_df = df[df['Annual Income (k$)'] > 60].sort_values(by = 'Annual Income (k$)', ascending = False)
print(sorted_df)

# Question 3: Create new columns to categorize customers based on their age and spending score.

# Categorize customers based on age
df['Age Group'] = pd.cut(df['Age'],bins = [0,30,50,100], labels=['Young', 'Middle-aged', 'Senior'])

# Categorize customers based on spending score
df['Spending Category'] = pd.cut(df['Spending Score (1-100)'], bins=[0,40,70,100], labels=['Low', 'Medium', 'High'])

# Question 4: Calculate the mean and median spending score for each age group and gender.

mean_spending = df.groupby(['Age','Gender'])['Spending Score (1-100)'].mean()
median_spending = df.groupby(['Age','Gender'])['Spending Score (1-100)'].median()
print(mean_spending)
print(median_spending)

# Question 5: Identify missing values in the dataset

missing_values = df.isnull().sum()
print(missing_values)

# Question 6: Use a pivot table to analyze the average spending score by gender and age group.

pivot_table = df.pivot_table(values = 'Spending Score (1-100)', index = 'Age Group', columns = 'Gender', aggfunc = 'mean')
print(pivot_table)

# Question 7: Visualize the distribution of customers' ages and annual income using matplotlib.

# Distribution of ages
import matplotlib.pyplot as plt
plt.hist(df['Age'], bins=15, color='skyblue', edgecolor='black')
plt.title("Distribution of Customers' Age")
plt.xlabel('Age')
plt.ylabel('Number of Customers')
plt.show()

# Distribution of annual income
plt.hist(df['Annual Income (k$)'], bins=15, color='lightgreen', edgecolor='black')
plt.title('Distribution of Annual Income')
plt.xlabel('Annual Income')
plt.ylabel('Number of Customers')
plt.show()

# Question 8: Visualize the relationship between annual income and spending score using a scatter plot.

plt.scatter(df['Annual Income (k$)'], df['Spending Score (1-100)'], color='blue')
plt.title('Annual Income vs. Spending Score')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.show()

# Question 9: Analyze changes in spending habits over different age groups using line plots.

# Average spending score by age group
spending_habits = df.groupby('Age Group')['Spending Score (1-100)'].mean()

# Plotting the spending habits
plt.plot(spending_habits.index, spending_habits.values, marker='o', color='purple')
plt.title('Spending Habits Across Different Age Groups')
plt.xlabel('Age Group')
plt.ylabel('Average Spending Score')
plt.show()

# Question 10: Compare the spending behavior of male and female customers using a bar plot.

# Average spending score by gender
gender_spending = df.groupby('Gender')['Spending Score (1-100)'].mean()

# Bar plot of spending by gender
plt.bar(gender_spending.index, gender_spending.values, color=["pink","blue"])
plt.title('Spending Behaviour by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Spending Score')
plt.show()



