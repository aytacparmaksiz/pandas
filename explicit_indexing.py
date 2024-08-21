import pandas as pd

# Creating the dataset
data = {
    'Student': ['John', 'Emily', 'Anna', 'Michael', 'Chris', 'David', 'Sophie', 'Liam'],
    'Class': ['1-A', '1-B', '1-A', '1-B', '2-A', '2-A', '2-B', '2-B'],
    'Math': [90, 85, 78, 92, 88, 76, 95, 89],
    'Science': [85, 88, 90, 86, 87, 91, 92, 93],
    'English': [78, 82, 80, 89, 84, 77, 91, 85]
}

df = pd.DataFrame(data)

# Setting index to students

df.set_index('Student', inplace = True)
print(df)

# Question 1: Display all the grades for the student "Michael."

michael_grades = df.loc["Michael"]
print(michael_grades)

# Question 2: Display the Math and Science grades for the students "Sophie" and "Liam."

sophie_liam_grades = df.loc[["Sophie", "Liam"], ["Math", "Science"]]
print(sophie_liam_grades)

# Question 3: Sort the dataset alphabetically by student names.

sorted_names = df.sort_index() # df.sort_index(level = "Student", ascending = True) with parameters.
print(sorted_names)

# Question 4: Sort the dataset by the Class column in descending order.

sorted_class = df.sort_values(by='Class', ascending=False)
print(sorted_class)

# Question 5: Reset the index and make the Class column as index. Sort the dataset by the Class column in ascending order.
# df.reset_index(inplace = True)

df.set_index("Class", inplace = True)
sorted_class_indexed = df.sort_index(level = "Class", ascending = True)
print(sorted_class_indexed)

# Question 6: Display the English grades for all students in class "1-A."

eng_grades_1_a = df.loc[["1-A"], ["Student", "English"]]
print(eng_grades_1_a)

# Question 7: List the Science and English grades for students with a Math score above 85.
# df.reset_index(inplace = True)
# df.set_index("Student", inplace = True)

high_scores = df.loc[df["Math"] > 85,  ["Science", "English"]]
print(high_scores)
