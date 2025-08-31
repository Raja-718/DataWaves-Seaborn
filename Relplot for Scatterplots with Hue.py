# Experiment 21: Relplot for Scatterplots with Hue
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.relplot(x="total_bill", y="tip", hue="sex", data=tips)
plt.suptitle("Relplot Scatter with Hue", y=1.02)
plt.show()
