# Experiment 10: Swarm Plot with Seaborn
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

plt.figure(figsize=(6,4))
sns.swarmplot(x="day", y="total_bill", data=tips, hue="sex", dodge=True)
plt.title("Swarm Plot of Total Bill by Day")
plt.show()
