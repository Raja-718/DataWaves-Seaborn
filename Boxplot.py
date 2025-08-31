# Experiment 7: Boxplot with Seaborn
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

plt.figure(figsize=(6,4))
sns.boxplot(x="day", y="total_bill", data=tips, hue="sex")
plt.title("Boxplot of Total Bill by Day & Sex")
plt.show()
