# Experiment 39: ECDF Plot
import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

plt.figure(figsize=(7,5))
sns.ecdfplot(data=iris, x="petal_length", hue="species", palette="Set1")
plt.title("Empirical Cumulative Distribution Function (ECDF)")
plt.show()
