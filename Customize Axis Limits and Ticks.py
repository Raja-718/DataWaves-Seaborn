# Experiment 14: Customize Axis Limits and Ticks
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

plt.figure(figsize=(6,4))
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.title("Custom Axis Example")
plt.xlim(0, 60)
plt.ylim(0, 12)
plt.xticks([0, 10, 20, 30, 40, 50, 60])
plt.yticks([0, 2, 4, 6, 8, 10, 12])
plt.show()
