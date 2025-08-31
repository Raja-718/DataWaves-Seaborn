# Experiment 20: Combine Multiple Style Settings
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.set_theme(style="whitegrid", context="talk", palette="Set2")

plt.figure(figsize=(7,5))
sns.lineplot(x="size", y="tip", data=tips, estimator="mean", marker="o")
plt.title("Lineplot with Combined Styling")
plt.show()
