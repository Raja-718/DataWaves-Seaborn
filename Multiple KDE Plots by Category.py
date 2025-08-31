# Experiment 33: Multiple KDE Plots by Category
import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

plt.figure(figsize=(7,5))
sns.kdeplot(data=iris, x="sepal_length", hue="species", fill=True, alpha=0.5, palette="coolwarm")
plt.title("Multiple KDE Plots by Species")
plt.show()
