# Experiment 23: Relplot with Row Facet
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.relplot(x="total_bill", y="tip", hue="smoker", row="sex", data=tips)
plt.suptitle("Relplot with Row Facet (Male vs Female)", y=1.05)
plt.show()
