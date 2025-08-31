# Experiment 19: Apply Custom Hex Colors
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

custom_colors = ["#FF5733", "#33C1FF"]  # Orange & Blue

plt.figure(figsize=(6,4))
sns.violinplot(x="day", y="tip", data=tips, hue="sex", palette=custom_colors, split=True)
plt.title("Violin Plot with Custom Hex Colors")
plt.show()
