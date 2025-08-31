# Experiment 13: Add Titles and Labels
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

plt.figure(figsize=(6,4))
sns.histplot(tips['total_bill'], bins=20, kde=True)
plt.title("Histogram of Total Bill", fontsize=14, fontweight="bold")
plt.xlabel("Total Bill Amount")
plt.ylabel("Frequency")
plt.show()
