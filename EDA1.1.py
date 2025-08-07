import pandas as pd
import seaborn as sns # type: ignore
import matplotlib.pyplot as plt # type: ignore
df=pd.read_csv("titanic_cleaned.csv")
# sns.countplot() is a Seaborn function used to plot the count (frequency) of each category in a column.
# sns.countplot(x='Survived', data=df)
# # Adds a title to the plot: "Survival Counts".
# plt.title('Survival Counts')
# # Adds a label to the x-axis.
# plt.xlabel('survived(0=No,1=Yes)')
# # Adds a label to the x-axis.
# plt.ylabel('Number of Passengers')
# # This tells Python to actually display the chart in a new window or output cell
# plt.show()
# # ou’ll see 2 bars for each gender: one for survied and another for non servivaed with two colours
# sns.countplot(x='Sex',hue='Survived', data=df)
# plt.title('Survival Count')
# plt.xlabel('Sex')
# plt.ylabel('Number of Passengers')
# plt.legend(title='Survived',labels=['NO','Yes'])

# plt.show()
# # Example data
# x = [1, 2, 3, 4, 5]
# y = [3, 5, 2, 8, 7]

# # Plotting
# plt.plot(x, y, marker='o', color='b', linestyle='-')  # line with circle markers
# plt.title('Basic love Chart')
# plt.xlabel('Maninder')
# plt.ylabel('Manpreet')
# plt.grid(True)
# plt.show()

data=[1,1,2]
unique_list = [x for x in data if x not in data and not data.add(x)]
print(unique_list)
# : Histogram Plot
plt.figure(figsize=(10,6))
sns.histplot(data=df, x='Age', hue='Survived', bins=30, kde=True, palette='Set1')
plt.title('Age Distribution by Survival')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()
