# Experiment 24: Lineplot with Multiple Lines
import seaborn as sns
import matplotlib.pyplot as plt

flights = sns.load_dataset("flights")

plt.figure(figsize=(8,5))
sns.lineplot(x="year", y="passengers", hue="month", data=flights)
plt.title("Lineplot of Passengers Over Years (Grouped by Month)")
plt.show()
