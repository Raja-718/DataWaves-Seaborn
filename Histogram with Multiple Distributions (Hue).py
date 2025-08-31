# Experiment 31: Histogram with Multiple Distributions (Hue)
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

plt.figure(figsize=(7,5))
sns.histplot(data=tips, x="total_bill", hue="sex", bins=20, kde=True, alpha=0.6, palette="Set2")
plt.title("Histogram with Multiple Distributions by Sex")
plt.show()
