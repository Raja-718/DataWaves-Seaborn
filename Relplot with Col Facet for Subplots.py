# Experiment 22: Relplot with Col Facet
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.relplot(x="total_bill", y="tip", hue="sex", col="time", data=tips)
plt.suptitle("Relplot with Column Facet (Lunch vs Dinner)", y=1.05)
plt.show()
