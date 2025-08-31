# Experiment 6: KDE Plot with Seaborn
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

plt.figure(figsize=(6,4))
sns.kdeplot(data=tips, x="total_bill", shade=True)
plt.title("KDE Plot of Total Bill")
plt.show()
