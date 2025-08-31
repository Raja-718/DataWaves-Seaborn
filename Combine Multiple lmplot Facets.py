# Experiment 30: Multiple lmplot Facets
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.lmplot(x="total_bill", y="tip", hue="sex", col="smoker", data=tips, height=5)
plt.suptitle("lmplot Facets by Sex and Smoker", y=1.05)
plt.show()
