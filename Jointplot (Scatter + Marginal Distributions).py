# Experiment 36: Jointplot (Scatter + Marginals)
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.jointplot(x="total_bill", y="tip", data=tips, kind="scatter", hue="sex", palette="Dark2")
plt.show()
