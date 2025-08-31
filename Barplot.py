# Experiment 2: Barplot with Seaborn
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

plt.figure(figsize=(6,4))
sns.barplot(x="day", y="total_bill", data=tips, estimator=sum, ci=None)
plt.title("Total Bill Sum by Day")
plt.show()
