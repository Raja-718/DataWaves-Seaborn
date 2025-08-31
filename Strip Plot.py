# Experiment 9: Strip Plot with Seaborn
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

plt.figure(figsize=(6,4))
sns.stripplot(x="day", y="total_bill", data=tips, jitter=True, hue="sex", dodge=True)
plt.title("Strip Plot of Total Bill by Day")
plt.show()
