# Experiment 4: Scatterplot with Seaborn
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

plt.figure(figsize=(6,4))
sns.scatterplot(x="total_bill", y="tip", data=tips, hue="sex")
plt.title("Scatterplot of Total Bill vs Tip")
plt.show()
