# Experiment 40: Displot with Multiple Facet Histograms
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.displot(data=tips, x="total_bill", col="sex", row="smoker", bins=20, hue="time", kde=True, palette="Set2")
plt.suptitle("Facet Histograms of Total Bill", y=1.02)
plt.show()
