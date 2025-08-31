# Experiment 26: Bubble Plot
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.relplot(x="total_bill", y="tip", size="size", hue="sex", data=tips, sizes=(20, 200))
plt.suptitle("Bubble Plot with Varying Sizes", y=1.02)
plt.show()
