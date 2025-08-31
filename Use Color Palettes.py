# Experiment 12: Use Color Palettes
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.set_palette("pastel")

plt.figure(figsize=(6,4))
sns.boxplot(x="day", y="total_bill", data=tips, hue="sex")
plt.title("Boxplot with Pastel Palette")
plt.show()
