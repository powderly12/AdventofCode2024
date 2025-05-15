import pandas as pd

# Extract the data from the CSV file
df = pd.read_csv('Data/LocationIDs.csv')

# Extract and sort the values of List1 and List2
list1_sorted = sorted(df['List1'])
list2_sorted = sorted(df['List2'])

# Compute the absolute differences and their sum
absolute_differences = [abs(a - b) for a, b in zip(list1_sorted, list2_sorted)]
sum_of_absolute_differences = sum(absolute_differences)

print("Distance between lists:", sum_of_absolute_differences)