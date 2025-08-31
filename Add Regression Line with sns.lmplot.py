# Experiment 29: Regression Line with lmplot
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.lmplot(x="total_bill", y="tip", data=tips, height=5)
plt.suptitle("Linear Regression Line with lmplot", y=1.02)
plt.show()
