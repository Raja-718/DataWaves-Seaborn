# Experiment 18: Change Figure Size Globally
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.set(rc={"figure.figsize":(8,6)})

sns.boxplot(x="day", y="tip", data=tips, hue="sex")
plt.title("Boxplot with Global Figure Size")
plt.show()
