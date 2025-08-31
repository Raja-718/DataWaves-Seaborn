# Experiment 8: Violin Plot with Seaborn
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

plt.figure(figsize=(6,4))
sns.violinplot(x="day", y="total_bill", data=tips, hue="sex", split=True)
plt.title("Violin Plot of Total Bill by Day & Sex")
plt.show()
