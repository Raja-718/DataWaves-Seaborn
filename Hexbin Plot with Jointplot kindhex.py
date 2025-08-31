# Experiment 38: Hexbin Plot with Jointplot
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.jointplot(x="total_bill", y="tip", data=tips, kind="hex", color="green", cmap="viridis")
plt.show()
